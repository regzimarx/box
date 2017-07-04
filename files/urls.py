from django.conf.urls import url

from .views import FileAPI

urlpatterns = [
    url(r'^upload/$', FileAPI.as_view({'post': 'upload'}), name='upload'),
    url(r'^files/$', FileAPI.as_view({'get': 'files'}), name='files'),
]