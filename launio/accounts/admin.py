from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import NewUser


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'last_name')
    list_filter = ('email', 'user_name', 'groups')
    ordering = ('id',)
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'is_superuser')}),
        ('Personal', {'fields': ('about', 'profile_image',)}),
    )

    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
