'use strict';

angular.
  module('burnItApp').
  config(['$locationProvider', '$routeProvider', '$httpProvider', function($locationProvider, $routeProvider, $httpProvider) {
      $routeProvider.
        when('/symbols', {
          template: '<symbol-list></symbol-list>'
        }).
        when('/symbol/:symbolId', {
          template: '<symbol-detail></symbol-detail>'
        }).
        otherwise('/symbols');

       $httpProvider.defaults.xsrfCookieName = 'csrftoken';
       $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);
