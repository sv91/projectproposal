  var myApp = angular.module('testModule',['hbpCommon']);
  myApp.controller('Controller', ['$scope', function($scope) {
      $scope.error= {
          code: 422,
          data: { email: [ 'Invalid e-mail address'] },
          message: 'Validation error.',
          type: 'Validation'
      };
      $scope.errorPermissions= {
          code: 403,
          message: 'Permission denied.',
          type: 'PermissionDenied'
      };
    }]);