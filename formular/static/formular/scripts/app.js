(function() {

// Define the formular application, currently doing nothing.
angular.module('formular', ['hbpCommon'])
.controller("Step3", function($scope){
})
.controller("Step5", function($scope){
})
.controller("Step6", function($scope){
})
.directive('singleUserSelect', function($log, hbpUserDirectory) {
	return {
	    scope: true,
		template: '<hbp-user-selector hbp-on-select="handleUserSelection"></hbp-user-selector><hbp-usercard hbp-user="selectedUser" ></hbp-usercard></pre>',
		link: function(scope, elt, attr) {
			// check if a user id is already set
			var userId = elt.parent().find('input').attr('value');
			if (userId) {
				hbpUserDirectory.get([userId])
				.then(function(users) {
					scope.selectedUser = users[userId];
				})
				.catch($log.error);
			}
			
			
			scope.selectedUser = null;
			scope.handleUserSelection = function(options) {
				console.log('select', arguments);
				scope.selectedUser = options.user;
				elt.parent().find('input').attr('value', scope.selectedUser.displayName);
				elt.parent().find('p').find('input').attr('value', scope.selectedUser.id);
			}
		}
	}
})
.directive('singleUserShow', function($log, hbpUserDirectory) {
	return {
	    scope: true,
		template: '<hbp-usercard hbp-user="selectedUser" ></hbp-usercard></pre>',
		link: function(scope, elt, attr) {
			// check if a user id is already set
			var userId = elt.parent().find('input').attr('value');
			if (userId) {
				hbpUserDirectory.get([userId])
				.then(function(users) {
					scope.selectedUser = users[userId];
				})
				.catch($log.error);
			}
			
			
			scope.selectedUser = null;
			scope.handleUserSelection = function(options) {
				console.log('select', arguments);
				scope.selectedUser = options.user;
				elt.parent().find('input').attr('value', scope.selectedUser.displayName);
				elt.parent().find('p').find('input').attr('value', scope.selectedUser.id);
			}
		}
	}
})
.directive('multiUserSelect', function() {
	return {
		scope: true,
		template: '<hbp-user-selector hbp-on-select="handleUserSelection"></hbp-user-selector><hbp-usercard ng-repeat="u in selectedUsers" hbp-user="u" ></hbp-usercard></pre>',
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