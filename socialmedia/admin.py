from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class CutsomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': (
            'avatar',
            'bio',
            'is_verified',
        )}),
    )


admin.site.register(get_user_model(), CutsomUserAdmin)
