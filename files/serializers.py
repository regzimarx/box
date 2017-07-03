from rest_framework import serializers

from .models import File

class FileSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ('file', 'user', 'date_uploaded')