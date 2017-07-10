(function () {
  'use strict';

  angular
    .module('box')
    .config(routes)

  /* UN AUTHENTICATED ROUTES
   */
  function routes ($urlMatcherFactoryProvider, $stateProvider,
    $locationProvider, $urlRouterProvider, TEMPLATE_URL) {

    $urlRouterProvider.otherwise('/');
    $urlMatcherFactoryProvider.strictMode(false);

    $stateProvider
      .state('legacy', {
        abstract : true,
        url      : '',
        template : '<ui-view></ui-view>'
      })
      .state('index', {
        url          : '/',
        templateUrl  : TEMPLATE_URL + 'index.html',
        controller   : 'IndexController',
        controllerAs : 'ctrl'
      })
    ;

  };

})();