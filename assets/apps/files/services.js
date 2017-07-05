(function(){

  angular
    .module('core')
    .service('FileService', FileService)
  ;

  function FileService($http, Upload) {

    var action = {
      upload   : upload,
      getFiles : getFiles,
      download : download,
      getFile  : getFile,
    }

    return action;

    function upload(file){
      return Upload.upload({
        url: '/api/upload/',
        data: {uploaded_file: file},
        method: 'POST'
      });
    }

    function getFiles(){
      return $http.get('/api/files/');
    }

    function download(unique_code){
      return $http.get('/api/download/' + unique_code);
    }

    function getFile(unique_code){
      return $http.get('/api/getFile/' + unique_code);
    }

  }

})();