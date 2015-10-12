/* global describe, it, expect, beforeEach, afterEach, jasmine, spyOn */
/* global module, inject, config */
/* global jso_registerRedirectHandler, jso_registerStorageHandler, jso_getToken, jso_ensureTokens, jso_Api_default_storage */

describe('bbpOidcSession', function() {
    'use strict';
    var bbpOidcSession, $httpBackend, $scope;
    beforeEach(function() {
        window.bbpConfig = {
            auth: {
                url: 'https://test.oidc.te/auth',
                clientId: 'test'
            }
        };
    });
    beforeEach(module('bbpOidcClient'));

    beforeEach(inject(function(_$httpBackend_, _$rootScope_, _bbpOidcSession_) {
        $httpBackend = _$httpBackend_;
        bbpOidcSession = _bbpOidcSession_;
        $scope = _$rootScope_;
    }));

    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();

        jso_registerStorageHandler(new jso_Api_default_storage());
    });

    it('should be defined', function() {
        expect(bbpOidcSession).toBeDefined();
        expect(bbpOidcSession.login).toBeDefined();
        expect(bbpOidcSession.logout).toBeDefined();
    });

    describe(".login()", function() {
        var redirectFunc;
        beforeEach(function() {
            redirectFunc = jasmine.createSpy('redirect');
            jso_registerRedirectHandler(redirectFunc);
        });

        it('should authenticate', function() {
            bbpOidcSession.login();
            expect(redirectFunc).toHaveBeenCalled();
        });

        it('should redirect to /authorize', function() {
            bbpOidcSession.login();
            expect(redirectFunc.calls.mostRecent().args[0])
            .toMatch(/\/authorize\?/);
        });

        describe("force prompt", function() {
            beforeEach(function() {
                bbpOidcSession.alwaysPromptLogin(true);
            });
            afterEach(function() {
                bbpOidcSession.alwaysPromptLogin(false);
            });

            it('should use prompt=login', function() {
                bbpOidcSession.login();
                expect(redirectFunc).toHaveBeenCalled();
                expect(redirectFunc.calls.mostRecent().args[0])
                .toMatch(/\/authorize\?prompt=login/);
            });
        });
    });

    describe(".logout()", function() {
        var storage, token, logoutUrl, tokenValue;
        beforeEach(function() {
            tokenValue = 'ABCD';
            storage = {
                getToken: function(domain) {
                    return token[domain];
                },
                wipeTokens: function(domain) {
                    delete token[domain];
                }
            };
            token = {
                'bbp': {
                    'access_token': tokenValue
                }
            };
            logoutUrl = 'https://test.oidc.te/auth/slo';
            jso_registerStorageHandler(storage);
            spyOn(window, 'jso_wipe').and.callThrough();
            expect(jso_getToken('bbp')).not.toBeNull();
            expect(jso_ensureTokens({'bbp':['openid']})).toBe(true);
            spyOn(storage, 'wipeTokens').and.callThrough();
            $httpBackend.when('POST', logoutUrl).respond(200);
        });

        it('should retrieve a promise', function() {
            var p = bbpOidcSession.logout();
            var resolved = false;
            p.then(function() {
                resolved = true;
            });
            expect(p.then).toBeDefined();
            $httpBackend.flush(1);
            expect(resolved).toBe(true);
        });

        it('should send a revocation request', function() {
            bbpOidcSession.logout();
            $httpBackend.expect('POST', logoutUrl, {token: tokenValue}, function(headers){
                return headers.Authorization === 'Bearer '+tokenValue;
            });
            $httpBackend.flush(1);
        });

        it('should wipe token', function() {
            bbpOidcSession.logout();
            $httpBackend.flush(1);
            expect(window.jso_wipe).toHaveBeenCalled();
            expect(storage.wipeTokens).toHaveBeenCalled();
        });

        it('should nullify actual token', function() {
            bbpOidcSession.logout();
            $httpBackend.flush(1);
            expect(window.jso_getToken('bbp')).toBeNull();
        });

        describe('then login', function() {
            var redirectFunc;

            beforeEach(function() {
                spyOn(bbpOidcSession, 'login');
            });

            it('should be triggered when ensureToken is true', function() {
                bbpOidcSession.ensureToken(true);
                bbpOidcSession.logout();
                $httpBackend.flush(1);
                expect(bbpOidcSession.login).toHaveBeenCalled();
            });

            it('should not be triggered when ensureToken is false', function() {
                bbpOidcSession.ensureToken(false);
                bbpOidcSession.logout();
                $httpBackend.flush(1);
                expect(bbpOidcSession.login).not.toHaveBeenCalled();
            });
        });
    });

    describe('.token()', function() {
        describe('before login', function() {
            it('should retrieve undefined', function() {
                expect(bbpOidcSession.token()).toBeNull();
            });
        });

        describe('after login', function() {
            var tokenValue, storage;
            beforeEach(function() {
                tokenValue = 'ABCD';
                storage = {
                    getToken: function() {
                        return {
                            'access_token': tokenValue
                        };
                    }
                };
                jso_registerStorageHandler(storage);
            });
            it('should retrieve the token', function() {
                expect(bbpOidcSession.token()).toBe(tokenValue);
            });
        });

    });
});
