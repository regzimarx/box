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

from .serializers import FileSerializer
from .models import File

class FileAPI(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def upload(self, data):
        serializer = FileSerializer(data=self.request.data)

        if serializer.is_valid():
            file = self.request.data.get('file')
            file_type = file.name.split('.')[-1]
            serializer.save(user=self.request.user, name=file.name, file_type=file_type)
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def files(self, data):
        files = File.objects.filter(user=self.request.user)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=HTTP_200_OK)