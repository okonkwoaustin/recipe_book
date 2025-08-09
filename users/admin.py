from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import customuser
from . forms import CustomUserChangeForm, UserRegistionForm


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistionForm
    form = CustomUserChangeForm
    model = customuser
    list_display = ["first_name", "last_name", "email",]
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')})
    )
    add_fieldsets = (
         (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )

    ordering = ("email",)
    search_fields = ("first_name",)


admin.site.register(customuser, CustomUserAdmin)