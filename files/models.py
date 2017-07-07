import string
import random

from django.db import models

def get_user_directory(instance, filename):
    return 'user_{}/{}'.format(instance.user.id, filename)

class FileUpload(models.Model):

    uploaded_file = models.FileField(upload_to=get_user_directory)
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=16)
    user = models.ForeignKey('users.User')
    unique_code = models.CharField(max_length=16, unique=True, default=None)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey('files.Folder', null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Folder(models.Model):

    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True)
    slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return '{}'.format(self.name)