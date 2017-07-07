from django.conf.urls import url

from .views import FileAPI

urlpatterns = [
    url(r'^upload/$', FileAPI.as_view({'post': 'upload'}), name='upload'),
    url(r'^files/$', FileAPI.as_view({'get': 'files'}), name='files'),
    url(r'^download/(?P<unique_code>\w+)', FileAPI.as_view({'get': 'download'}), name='download'),
    url(r'^getFile/(?P<unique_code>\w+)', FileAPI.as_view({'get': 'getFile'}), name='get-file'),
]