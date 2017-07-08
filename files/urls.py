from django.conf.urls import url

from .views import FileAPI, FolderAPI

urlpatterns = [
    url(r'^upload/$', FileAPI.as_view({'post': 'upload'}), name='upload'),
    url(r'^download/(?P<unique_code>\w+)', FileAPI.as_view({'get': 'download'}),
        name='download'),
    url(r'^getFile/(?P<unique_code>\w+)', FileAPI.as_view({'get': 'get_file'}),
        name='get-file'),
    url(r'^newFolder/', FolderAPI.as_view({'post': 'new_folder'}),
        name='new-folder'),
    url(r'^files/$', FileAPI.as_view({'get': 'files'}), name='files'),
    url(r'^folders/$', FolderAPI.as_view({'get': 'folders'}), name='folders'),
    url(r'^folders/(?P<folder_slug>[-\w]+)$', FolderAPI.as_view({'get': 'folder_folders'}),
        name='folder-folders'),
    url(r'^files/(?P<folder_slug>[-\w]+)$', FolderAPI.as_view({'get': 'folder_files'}),
        name='folder-files'),
]