import string
import random
import mimetypes
import urllib

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
from django.http import HttpResponse
from django.conf import settings

from .serializers import FileSerializer
from .models import FileUpload

class FileAPI(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def upload(self, *args, **kwargs):
        serializer = FileSerializer(data=self.request.data)

        if serializer.is_valid():
            uploaded_file = self.request.data.get('uploaded_file')
            file_type = uploaded_file.name.split('.')[-1]
            serializer.save(user=self.request.user, name=uploaded_file.name,
                            file_type=file_type, unique_code=self.generate_unique_code(code_length=16))
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def files(self, *args, **kwargs):
        
        files = FileUpload.objects.filter(user=self.request.user)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def download(self, *args, **kwargs):

        download_file = get_object_or_404(FileUpload, unique_code=kwargs.get('unique_code'))
        file_content_type = mimetypes.guess_type(download_file.name)[0]
        file_path = settings.BASE_DIR + download_file.uploaded_file.url
        print(settings.BASE_DIR)
        with open(file_path, 'rb') as fp:
            data = fp.read()
        filename = download_file.name
        response = HttpResponse(content_type=file_content_type)
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        response.write(data)
        return response

    def getFile(self, *args, **kwargs):
        download_file = get_object_or_404(FileUpload, unique_code=kwargs.get('unique_code'))
        serializer = FileSerializer(download_file)
        return Response(serializer.data, status=HTTP_200_OK)


    def generate_unique_code(self, code_length):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(code_length))