/* global jso_configure, jso_ensureTokens, jso_getToken, jso_dump, jso_wipe */
(function(){
    'use strict';

    var options, initialized, _alwaysPromptLogin, _ensureToken, config;

    var init = function() {
        if (initialized) {
            return;
        }
        options = {
            clientId: config.get('auth.clientId'),
            authServer: config.get('auth.url'),
            debug: config.get('oidc.debug', false),
            redirectUri: document.URL,
            scopes: ['openid'],
            jsonWebKeys: {'keys':[{'alg':'RS256','e':'AQAB','n':'zlJpDPnGMUV5FlwQs5eIs77pdZTST29TELUT3_E1sKrN-lE4rEgbQQ5qU1KvF5669VmVeAt-BQ2qMjGjUyl44gq-aUkeQV7MXfYJfKHIULZMTGR0lJ4ebPRQgM5OWDNjYVbASAOz0NyO646G5H5BlHZrA9ADyrZYZ4CEhfI1KBk','kty':'RSA','kid':'bbp-oidc'}]}
        };
        // If we need to generate the options, we need
        // to bootstrap jso as well.
        // It would be better to run this into a module bootstrap phase
        // but for now the bbpConfig service does not load early enough.
        // It should be a constant probably.
        jso_configure({
            'bbp': {
                client_id: options.clientId,
                redirect_uri: options.redirectUri,
                authorization: options.authServer+'/authorize'+(
                    _alwaysPromptLogin ? '?prompt=login' : ''
                ),
                auth_server: options.authServer+'/',
                jsonWebKeys: options.jsonWebKeys
            }
        },{
            'debug': options.debug,
            'token': null
        });

        // This check has to occurs every time.
        if (_ensureToken) {
            if(!jso_getToken('bbp', options.scopes)) {
                // if there's no token, check if the session with oidc is still active
                isSessionActive(function(active) {
                    if(!active) {
                        // notify the parent window that a new login is needed
                        postLogoutMsg(options.clientId);
                    }
                    // ensure token in any case
                    // if active == true, it will get a new token, otherwise redirect to login
                    jso_ensureTokens({'bbp': options.scopes});
                });
            }
        }

        initialized = true;
    };

    var postLogoutMsg = function(clientId) {
        if(window.parent && window !== window.top) {
            window.parent.postMessage({
                eventName: 'oidc.logout',
                data: {
                    clientId: clientId
                }
            }, '*');
        }
    };

    var isSessionActive = function(callback) {
        var oReq = new XMLHttpRequest();
        oReq.onload = function() {
            if(callback) {
                callback(this.status === 200);
            }
        };

        oReq.open('get', options.authServer + '/session', true);
        oReq.withCredentials = true;
        oReq.send();
    };

    angular.module('bbpOidcClient', ['bbpConfig'])
        .config(['bbpConfig', function(bbpConfig) {
            config = bbpConfig;
            init();
        }])
        .config(['$httpProvider', function ($httpProvider) {
            $httpProvider.interceptors.push('httpOidcRequestInterceptor');
            init();
        }])
        .provider('bbpOidcSession', function() {
            /**
             * Ensure that we will always prompt the login.
             *
             * @param {Boolean} value truthy if a login prompt should be
             *        forced when a token needs to be retrieved.
             */
            this.alwaysPromptLogin = function(value) {
                _alwaysPromptLogin = !!value;
                initialized = false;
                init();
            };

            this.ensureToken = function(value) {
                _ensureToken = !!value;
                initialized = false;
                init();
            };

            this.$get = ['$http', '$log', '$q', 'bbpConfig', function($http, $log, $q, bbpConfig) {
                return {
                    logout: function() {
                        var self = this;
                        // Ensure we have a token.
                        var token = this.token();
                        var localRemoval = function() {
                            // We need to keep the token to generate
                            // Bearer for this request. Hence the reset only after.
                            jso_wipe();

                            if (_ensureToken) {
                                self.login();
                            }
                        };

                        return $http({
                            method: 'POST',
                            url: options.authServer+'/slo',
                            data: { token: token },
                            withCredentials: true
                        }).then(localRemoval, localRemoval);
                    },
                    login: function() {
                        return jso_ensureTokens({'bbp': options.scopes});
                    },
                    token: function() {
                        return jso_getToken('bbp', options.scopes);
                    },
                    alwaysPromptLogin: this.alwaysPromptLogin,
                    ensureToken: this.ensureToken
                };
            }];
        })
        // authentication and request token injection
        .factory('httpOidcRequestInterceptor', ['bbpConfig', '$log', '$q', '$window',
            function (bbpConfig, $log, $q, $window) {
            return {
                request: function (requestConfig) {
                    var token = jso_getToken('bbp', options.scopes);
                    if (token) {
                        requestConfig.headers.Authorization = 'Bearer ' + token;
                    } else if(_ensureToken) {
                        jso_ensureTokens({'bbp': options.scopes});
                    }

                    return requestConfig;
                },
                responseError: function(rejection) {
                    // if we have a Authorization token and got a 401, we should logout, and try the request again
                    var headers = rejection.config.headers;
                    if (headers && headers.Authorization && rejection.status === 401) {
                        $log.debug('current token is not valid anymore:', rejection.data);
                        // remove token from localStorage
                        jso_wipe();
                        // notifiy parent window
                        postLogoutMsg();
                        // trigger authentication if needed
                        if (_ensureToken) {
                            jso_ensureTokens({'bbp': options.scopes});
                        }
                    }
                    return $q.reject(rejection);
                }
            };
        }]);
}());
