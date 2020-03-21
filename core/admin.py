from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email', 'mobile']
    fieldsets = (
        (None, {
            "fields": (
                'username',
                'email',
                'mobile',
                'password',
            ),
        }),
        # (_('Personal Info'), {
        #     "fields": (
        #         'first_name',
        #         'middle_name',
        #         'last_name',
        #         'gender',
        #         'dob',
        #     )
        # }),
        (_('Permissions'), {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
                'is_verified',
            )
        }),
        (_('Important Dates'), {
            "fields": (
                'last_login',
            )
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'mobile',
                'password1',
                'password2',
            )
        }),
    )
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)
