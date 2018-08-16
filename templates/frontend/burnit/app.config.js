'use strict';

angular.
  module('burnItApp').
  config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $routeProvider.
        when('/symbol-list', {
          template: '<symbol-list></symbol-list>'
        }).
        when('/symbol-description', {
          template: '<symbol-description></symbol-description>'
        }).
        otherwise('/symbol-list');
    }
  ]);
