from django.db import models

def get_user_directory(instance, filename):
    return 'user_{}/{}'.format(instance.user.id, filename)

class FileUpload(models.Model):

    uploaded_file = models.FileField(upload_to=get_user_directory)
    name = models.CharField(max_length=225)
    file_type = models.CharField(max_length=16)
    user = models.ForeignKey('users.User')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)
