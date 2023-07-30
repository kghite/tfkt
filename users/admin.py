from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users import forms
from users.models import User


class UserAdmin(BaseUserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    list_display = ("email",)
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {"fields": ("email", "s", "password")}),
        ("Permissions", {"fields": ("is_staff",)}),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("email", "password", "password2", "is_staff", "is_superuser")},
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
