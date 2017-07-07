from django.contrib import admin

from .models import FileUpload, Folder

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_code', 'user', 'date_uploaded',)


class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'parent', 'slug')

admin.site.register(FileUpload, FileAdmin)
admin.site.register(Folder, FolderAdmin)
