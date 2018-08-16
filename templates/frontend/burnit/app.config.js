'use strict';

angular.
  module('burnItApp').
  config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $routeProvider.
        when('/symbol-list', {
          template: '<symbol-list></symbol-list>'
        }).
        when('/phones1', {
          template: 'world'
        }).
        otherwise('/symbol-list');
    }
  ]);