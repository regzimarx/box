(function(){
  'use strict';

  angular
    .module('core')
    .controller('UploadController', UploadController)
    .controller('DownloadController', DownloadController)
  ;

  function UploadController($scope, $location, $stateParams, Upload, FileService, FolderService){
    var self = this;
    $scope.baseUrl = window.location.host;
    var folder_slug = $stateParams.folder_slug;

    if (folder_slug == undefined){
      var folder_slug = '';
    }

    FileService.getFiles(folder_slug).then(function(resp){
      $scope.userFiles = resp.data;
    }).catch(function(errors){
      $scope.FileErrors = errors.data;
    });

    FolderService.getFolders(folder_slug).then(function(resp){
      $scope.folders = resp.data;
    }).catch(function(errors){
      $scope.folderErrors = errors.data;
    });

    $scope.$watch('files', function(){
      self.upload($scope.files);
    });

    self.upload = function(files){
      angular.forEach(files, function(file){

        FileService.upload(file, folder_slug).then(function(resp){
          $scope.userFiles.push(resp.data)
        }).catch(function(error){
          $scope.error = error;
        });
        
      });
    }

    self.download = function(unique_code){
      FileService.download(unique_code);
    }

    self.newFolder = function(folderName){

      FileService.newFolder(folderName, folder_slug).then(function(resp){
        $scope.folders.push(resp.data)
      }).catch(function(errors){
        $scope.errors = errors.data;
      });
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