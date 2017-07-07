(function(){
  'use strict';

  angular
    .module('core')
    .controller('UploadController', UploadController)
    .controller('DownloadController', DownloadController)
  ;

  function UploadController($scope, $location, Upload, FileService){
    var self = this;
    $scope.baseUrl = $location.absUrl();

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

    self.download = function(unique_code){
      FileService.download(unique_code);
    }

  }

  function DownloadController($scope, $stateParams, FileService){

    var self = this;

    FileService.getFile($stateParams.unique_code).then(function(resp){
      $scope.data = resp.data;
    }).catch(function(error){
      $scope.error = error;
    })

    self.download = function(unique_code){
      FileService.download(unique_code);
    }

  }

})();