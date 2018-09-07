'use strict';

angular.
  module('symbol').
  factory('Symbol', ['$resource',
    function($resource) {
      return $resource('/:symbolId', {}, {
        query: {
          method: 'GET',
          params: {symbolId: 'api/gallery/'},
          isArray: true
        }
      });
    }
  ]);
