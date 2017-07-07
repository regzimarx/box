(function(){

  angular
    .module('core')
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

    function upload(file, folder){
      return Upload.upload({
        url: '/api/upload/',
        data: {uploaded_file: file, folder: folder},
        method: 'POST'
      });
    }

    function getFiles(folder_id) {
      return $http.get('/api/files/' + folder_id);
    }

    function download(unique_code){
      var hostUrl = window.location.host;
      window.open('/api/download/' + unique_code);
    }

    function getFile(unique_code){
      return $http.get('/api/getFile/' + unique_code);
    }

    function newFolder(folderName, folder){
      data = {name: folderName, parent: folder}
      return $http.post('/api/newFolder/', data);
    }

  }


  function FolderService($http){

    var actions = {
      getFolders     : getFolders,
    }

    return actions;

    function getFolders(folder_id) {
      return $http.get('/api/folders/' + folder_id);
    }

  }

})();