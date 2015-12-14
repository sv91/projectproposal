(function() {

// Define the formular application, currently doing nothing.
angular.module('formular', ['hbpCommon'])
.controller("Step3", function($scope){
})
.directive('singleUserSelect', function() {
	return {
	    scope: true,
		template: '<hbp-user-selector hbp-on-select="handleUserSelection"></hbp-user-selector><hbp-usercard hbp-user="selectedUser" ></hbp-usercard><pre ng-bind="selectedUser | json"></pre>',
		link: function(scope, elt, attr) {
			scope.selectedUser = null;
			scope.handleUserSelection = function(options) {
				console.log('select', arguments);
				scope.selectedUser = options.user;
				elt.parent().find('input').attr('value', scope.selectedUser.id);
			}
		}
	}
})
.directive('multiUserSelect', function() {
	return {
		scope: true,
		template: '<hbp-user-selector hbp-on-select="handleUserSelection"></hbp-user-selector><hbp-usercard ng-repeat="u in selectedUsers" hbp-user="u" ></hbp-usercard><pre ng-bind="selectedUser | json"></pre>',
		link: function(scope, elt, attr) {
			scope.selectedUsers = [];
			scope.handleUserSelection = function(options) {
				console.log('select', arguments);
				scope.selectedUsers.push(options.user);
				// TODO: elt.parent().find('input').attr(value, scope.selectedUser);
			}
		}
	}
});

// Bootstrap function
angular.bootstrap().invoke(function($http, $log) {
  $http.get('config.json').then(function(res) {
    window.bbpConfig = res.data;
    angular.element(document).ready(function() {
      angular.bootstrap(document, ['formular']);
    });
  }, function() {
    $log.error('Cannot boot formular application');
  });
});

}());