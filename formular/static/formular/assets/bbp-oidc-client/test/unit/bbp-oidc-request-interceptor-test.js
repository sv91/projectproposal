/* global describe, it, expect, beforeEach, afterEach, jasmine, spyOn */
/* global module, inject, config */
/* global jso_registerRedirectHandler, jso_registerStorageHandler, jso_getToken, jso_ensureTokens */
/* global jso_Api_default_storage */

describe('bbpOidcRequestInterceptor', function() {
    'use strict';

    var $http, $httpBackend, url, bbpOidcSession, sessionStatusUrl;

    beforeEach(function() {
        window.bbpConfig = {
            auth: {
                url: 'https://test.oidc.te/auth',
                clientId: 'test'
            },
            oidc: {
                debug: false
            }
        };
        sessionStatusUrl = window.bbpConfig.auth.url + '/session';
    });

    beforeEach(function() {
        url = 'http://onehundredcoverage.com';
        module('bbpOidcClient');
        spyOn(window.parent, 'postMessage');
    });

    beforeEach(function() {
      jasmine.Ajax.install();
    });

    afterEach(function() {
      jasmine.Ajax.uninstall();
    });

    beforeEach(inject(function(_$http_, _$httpBackend_, _bbpOidcSession_) {
        $http = _$http_;
        $httpBackend = _$httpBackend_;
        bbpOidcSession = _bbpOidcSession_;
    }));

    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
        jso_registerStorageHandler(new jso_Api_default_storage());
    });

    describe('with a token', function() {

        beforeEach(function() {
            jso_registerStorageHandler({
                getToken: function() {
                    return { access_token: 'ABCD' };
                }
            });
            spyOn(window, 'jso_wipe').and.returnValue(true);
        });

        it('set Authorization header', function() {
            $http.get(url);
            $httpBackend.expect('GET', url, null, function(headers) {
                return headers.Authorization === 'Bearer ABCD';
            }).respond(200);
            $httpBackend.flush();

            expect(window.jso_wipe).not.toHaveBeenCalled();
        });

        it('should wipe the token on 401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url, null, function(headers) {
                return headers.Authorization === "Bearer ABCD";
            }).respond(401);
            $httpBackend.flush();

            expect(window.jso_wipe).toHaveBeenCalled();
        });

        it('should post a logout request to parent windows on 401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url, null, function(headers) {
                return headers.Authorization === "Bearer ABCD";
            }).respond(401);
            $httpBackend.flush();

            expect(window.parent.postMessage).toHaveBeenCalled();
        });

        it('should not wipe the token on !401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url, null, function(headers) {
                return headers.Authorization === "Bearer ABCD";
            }).respond(403);
            $httpBackend.flush();

            expect(window.jso_wipe).not.toHaveBeenCalled();
        });

        it('should not post a logout request to parent windows on !401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url, null, function(headers) {
                return headers.Authorization === "Bearer ABCD";
            }).respond(200);
            $httpBackend.flush();

            expect(window.parent.postMessage).not.toHaveBeenCalled();
        });
    });

    describe('without a token', function() {
        beforeEach(function() {
            jso_registerStorageHandler({
                getToken: function() {
                    return null;
                },
                saveState: function() {}
            });

            spyOn(window, 'jso_ensureTokens').and.returnValue(null);
            spyOn(window, 'jso_wipe').and.returnValue(true);
        });

        it('set no Authorization header', function() {
            $http.get(url);
            $httpBackend.expect('GET', url, null, function(headers) {
                return headers.Authorization === undefined;
            }).respond(200);
            $httpBackend.flush();
        });

        it('if needed, tries to get a new one', function() {
            bbpOidcSession.ensureToken(true);
            window.jso_ensureTokens.calls.reset();

            $http.get(url);
            $httpBackend.expect('GET', url).respond(200);
            $httpBackend.flush();
            expect(window.jso_ensureTokens).toHaveBeenCalled();
        });

        it('if not needed, doesn\'t try to get a new one', function() {
            bbpOidcSession.ensureToken(false);
            window.jso_ensureTokens.calls.reset();

            $http.get(url);
            $httpBackend.expect('GET', url).respond(200);
            $httpBackend.flush();

            expect(window.jso_ensureTokens).not.toHaveBeenCalled();
        });

        it('if no active session, should post a logout request to parent windows', function() {
            jasmine.Ajax.stubRequest(sessionStatusUrl).andReturn({
                status: 404
            });

            bbpOidcSession.ensureToken(true);
            window.jso_ensureTokens.calls.reset();

            $http.get(url);
            $httpBackend.expect('GET', url).respond(200);
            $httpBackend.flush();

            expect(window.parent.postMessage).toHaveBeenCalled();
        });

        it('if active session, shoudld not post a logout request to parent windows', function() {
            jasmine.Ajax.stubRequest(sessionStatusUrl).andReturn({
                status: 200
            });

            bbpOidcSession.ensureToken(true);
            window.jso_ensureTokens.calls.reset();

            $http.get(url);
            $httpBackend.expect('GET', url).respond(200);
            $httpBackend.flush();

            expect(window.parent.postMessage).not.toHaveBeenCalled();
        });

        it('should not wipe the token on 401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url).respond(401);
            $httpBackend.flush();

            expect(window.jso_wipe).not.toHaveBeenCalled();
        });

        it('should not post a logout request to parent windows on 401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url).respond(401);
            $httpBackend.flush();

            expect(window.parent.postMessage).not.toHaveBeenCalled();
        });

        it('should not wipe the token on !401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url).respond(403);
            $httpBackend.flush();

            expect(window.jso_wipe).not.toHaveBeenCalled();
        });

        it('should not post a logout request to parent windows on !401 error', function() {
            $http.get(url);
            $httpBackend.expect('GET', url).respond(200);
            $httpBackend.flush();

            expect(window.parent.postMessage).not.toHaveBeenCalled();
        });
    });

});
