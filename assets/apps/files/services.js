(function(){

  angular
    .module('core')
    .service('FileService', FileService)
  ;

  function FileService ($http, Upload) {

    var action = {
      upload : upload,
      getFiles  : getFiles,
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

  }

})();