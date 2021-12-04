from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

UserAdmin.fieldsets[2][1]['fields'] = (
        'is_active', 
        'is_staff', 
        'is_superuser',
        'Is_Author',
        'Special_User',
        'groups', 
        'user_permissions',
)

UserAdmin.list_display += ('Is_Author', 'is_special_user')
admin.site.register(User, UserAdmin)