(function(){
  'use strict';

  angular
    .module('core')
    .config(routes)
  ;

  /*
    ROUTES FOR AUTHENTICATED USERS
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
      .state('home', {
        url          : '/',
        templateUrl  : TEMPLATE_URL + 'home.html',
        controller   : 'UploadController',
        controllerAs : 'ctrl'
      })
      .state('download', {
        url          : '/file/:unique_code/',
        templateUrl  : TEMPLATE_URL + 'download.html',
        controller   : 'DownloadController',
        controllerAs : 'ctrl'
      })
      .state('folder', {
        url          : '/:folder_id',
        templateUrl  : TEMPLATE_URL + 'home.html',
        controller   : 'UploadController',
        controllerAs : 'ctrl'
      })
    ;
  }

})();