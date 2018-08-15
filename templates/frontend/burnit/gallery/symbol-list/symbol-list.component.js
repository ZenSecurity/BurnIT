'use strict';

angular.module('symbolList').
    component('symbolList', {
    templateUrl: 'static/frontend/burnit/gallery/symbol-list/symbol-list.template.html',
    controller: function symbolListController() {
      this.symbols = [
          '1',
          '2',
          '3'
      ];
    }
});
