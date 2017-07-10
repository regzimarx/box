(function(){

  angular
    .module('box')
    .service('FileService', FileService)
    .service('FolderService', FolderService)
  ;

  function FileService($http, Upload) {

    var action = {
      upload   : upload,
      getFiles : getFiles,
      download : download,
      getFile  : getFile,
      newFolder: newFolder
    }

    return action;

    function upload(file, folder_slug){
      return Upload.upload({
        url: '/api/upload/',
        data: {uploaded_file: file, folder: folder_slug},
        method: 'POST'
      });
    }

    function getFiles(folder_slug) {
      return $http.get('/api/files/' + folder_slug);
    }

    function download(unique_code){
      var hostUrl = window.location.host;
      window.open('/api/download/' + unique_code);
    }

    function getFile(unique_code){
      return $http.get('/api/getFile/' + unique_code);
    }

    function newFolder(folderName, folder){
      var data = {name: folderName, parent: folder}
      return $http.post('/api/newFolder/', data);
    }

  }


  function FolderService($http){

    var actions = {
      getFolders     : getFolders
    }

    return actions;

    function getFolders(folder_slug) {
      return $http.get('/api/folders/' + folder_slug);
    }

  }

})();