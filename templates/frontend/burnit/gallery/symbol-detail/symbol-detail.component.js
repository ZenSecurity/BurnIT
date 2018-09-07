'use strict';

angular.module('symbolDetail').
    component('symbolDetail', {
    templateUrl: 'static/frontend/burnit/gallery/symbol-detail/symbol-detail.template.html',
    controller: ['$routeParams', '$http', 'Symbol', function symbolDetailController($routeParams, $http, Symbol) {
        var self = this;
        self.symbol = Symbol.get({symbolId: "api/gallery/"+$routeParams.symbolId+"/"});

        self.burn = function() {
	    $http.post('/api/user/', {"name": self.name}).then(function(response) {
                self.response = response.data;
	   }).then(function(data){
		   $http.post('/api/poll/', {"user": {"id": self.response.id, "name": self.response.name}, "symbol": {"id": $routeParams.symbolId}});
	   });

	}
    }]
});
