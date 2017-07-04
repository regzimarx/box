from django.contrib import admin

from .models import FileUpload

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date_uploaded')

admin.site.register(FileUpload, FileAdmin)
