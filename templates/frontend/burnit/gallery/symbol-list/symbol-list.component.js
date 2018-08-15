'use strict';

angular.module('symbolList').
    component('symbolList', {
    templateUrl: 'static/frontend/burnit/gallery/symbol-list/symbol-list.template.html',
    controller: function symbolListController($http) {
        var self = this;

        $http.get('api/gallery/').then(function(response) {
            self.symbols = response.data;
      });
    }
});
