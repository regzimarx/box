from django.db import models
from django.conf import settings

def get_user_directory(instance, filename):
    return '{}/{}'.format(instance.user.email, filename)

class File(models.Model):

    file = models.FileField(upload_to=get_user_directory)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.file)