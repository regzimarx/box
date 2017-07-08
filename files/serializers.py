from rest_framework import serializers

from .models import FileUpload, Folder

class FileSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    uploaded_file = serializers.FileField()

    class Meta:
        model = FileUpload
        fields = ('id', 'uploaded_file', 'name', 'file_type', 'user', 'unique_code', 'date_uploaded', 'folder',)
        read_only_fields = ('id', 'name', 'file_type', 'unique_code', 'folder')


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ('id', 'name', 'parent', 'date_created', 'slug',)
        read_only_fields = ('id', 'slug', 'parent')