'use strict';

angular.module('symbolList').
    component('symbolList', {
    templateUrl: 'static/frontend/burnit/gallery/symbol-list/symbol-list.template.html',
    controller: ['Symbol', function symbolListController(Symbol) {
	this.symbols = Symbol.query();
    }]
});
