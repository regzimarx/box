from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff',)

    fieldsets = (
        ('User details', {'fields': ('email', 'password', 'first_name', 'last_name',)}),
        ('User status', {'fields': ('is_active', 'is_staff',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'is_staff', 
            'is_active', 'password1', 'password2',)}),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
