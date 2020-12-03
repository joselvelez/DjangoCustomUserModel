from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdminConfig(UserAdmin):
    search_fields                       = ('email', 'user_name', 'first_name', 'last_name',)
    list_filter                         = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff',)
    ordering                            = ('-join_date',)
    list_display                        = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff', 'join_date')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_superuser',)}),
        ('Personal', {'fields': ('about', 'tagline', 'website', 'privacy_email', 'privacy_library',)}),
        ('Media', {'fields': ('profile_image', 'profile_background',)}),
    )

    # formfield_overrides = {
    #     CustomUser.about: {'widget': Textarea()},
    # }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )

admin.site.register(CustomUser, CustomUserAdminConfig)