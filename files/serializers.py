from rest_framework import serializers

from .models import FileUpload

class FileSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    uploaded_file = serializers.FileField()

    class Meta:
        model = FileUpload
        fields = ('uploaded_file', 'name', 'file_type', 'user', 'date_uploaded')
        read_only_fields = ('name', 'file_type')