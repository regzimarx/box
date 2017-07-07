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
    var folder_id = $stateParams.folder_id;

    if (folder_id == undefined){
      var folder_id = '';
    }

    FileService.getFiles(folder_id).then(function(resp){
      $scope.userFiles = resp.data;
    }).catch(function(errors){
      $scope.FileErrors = errors.data;
    });

    FolderService.getFolders(folder_id).then(function(resp){
      $scope.folders = resp.data;
    }).catch(function(errors){
      $scope.folderErrors = errors.data;
    });

    $scope.$watch('files', function(){
      self.upload($scope.files);
    });

    self.upload = function(files){
      var folder = $stateParams.folder_id;
      angular.forEach(files, function(file){

        FileService.upload(file, folder).then(function(resp){
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
      var folder = $stateParams.folder_id;

      FileService.newFolder(folderName, folder).then(function(resp){
        $scope.folders.push(resp.data)
      }).catch(function(errors){
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