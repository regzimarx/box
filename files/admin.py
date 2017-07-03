from django.contrib import admin

from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date_uploaded')

admin.site.register(File, FileAdmin)
