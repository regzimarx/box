from rest_framework import serializers

from .models import File

class FileSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ('file', 'name', 'file_type', 'user', 'date_uploaded')
        read_only_fields = ('name', 'file_type')