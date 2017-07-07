import string
import random
import mimetypes
import os

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)
from rest_framework.permissions import (
    IsAuthenticated
)
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from wsgiref.util import FileWrapper
from django.utils.text import slugify

from .serializers import FileSerializer, FolderSerializer
from .models import FileUpload, Folder

class FileAPI(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def upload(self, *args, **kwargs):
        serializer = FileSerializer(data=self.request.data)

        if serializer.is_valid():
            uploaded_file = self.request.data.get('uploaded_file')
            file_type = uploaded_file.name.split('.')[-1]

            serializer.save(
                user=self.request.user, name=uploaded_file.name,
                file_type=file_type,
                unique_code=self.generate_unique_code(code_length=16),
            )
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def files(self, *args, **kwargs):
        
        files = FileUpload.objects.filter(user=self.request.user, folder=None)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    def download(self, *args, **kwargs):

        download_file = get_object_or_404(FileUpload, unique_code=kwargs.get('unique_code'))
        file_path = '{}{}'.format(settings.BASE_DIR, download_file.uploaded_file.url)

        if os.path.exists(file_path):
            file_content_type = mimetypes.guess_type(file_path)[0]
            file_wrapper = FileWrapper(open(file_path, 'rb'))

            response = HttpResponse(file_wrapper, content_type=file_content_type)
            response['Content-Disposition'] = 'attachment; filename={}'.format(download_file.name)

            return response

        return HttpResponseNotFound('<h3>File not found</h5>')


    def get_file(self, *args, **kwargs):
        download_file = get_object_or_404(FileUpload, unique_code=kwargs.get('unique_code'))
        serializer = FileSerializer(download_file)
        return Response(serializer.data, status=HTTP_200_OK)


    def generate_unique_code(self, code_length):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(code_length))


class FolderAPI(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def new_folder(self, *args, **kwargs):

        if Folder.objects.filter(
            name__exact=self.request.data.get('name'),
            parent__id=self.request.data.get('parent')
            ).exists():
            data = {'error': 'Folder already exists.'}
            return Response(data, status=HTTP_400_BAD_REQUEST)

        serializer = FolderSerializer(data=self.request.data)

        if serializer.is_valid():
            serializer.save(slug=slugify(self.request.data.get('name')))
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def folders(self, *args, **kwargs):
        folder_id = kwargs.get('folder_id')
        folders = Folder.objects.filter(parent=kwargs.get('folder_id'))
        serializer = FolderSerializer(folders, many=True)

        return Response(serializer.data, status=HTTP_200_OK)


    def folder_files(self, *args, **kwargs):

        files = FileUpload.objects.filter(user=self.request.user, 
            folder=kwargs.get('folder_id'))
        serializer = FileSerializer(files, many=True)
        # import pdb; pdb.set_trace()
        return Response(serializer.data, status=HTTP_200_OK)
