(function(){
  'use strict';

  angular
    .module('core')
    .controller('UploadController', UploadController)
  ;

  function UploadController($scope, Upload, FileService){
    var self = this;

    FileService.getFiles().then().then(function(resp){
      $scope.data = resp.data;
    }).catch(function(error){
      $scope.error = error;
    });

    $scope.$watch('files', function(){
      self.upload($scope.files);
    });

    self.upload = function(files){

      angular.forEach(files, function(file){

        FileService.upload(file).then(function(resp){
          $scope.data.push(resp.data)
        }).catch(function(error){
          $scope.error = error;
        });
        
      });

    }

  }

})();