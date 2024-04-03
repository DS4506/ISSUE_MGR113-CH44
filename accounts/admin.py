from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username", "email", "last_name", "first name",
        "role", "team", "is_staff"
    ]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("None", {"fields": ("role","team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
         ("None", {"fields": ("role","team")}),
    )
    
    admin.siteregister(CustomUser, CustomUserAdmin)
