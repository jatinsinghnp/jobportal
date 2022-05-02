from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import SingUpForm, UserChangeForm
from django.contrib import admin


class UserAmdin(BaseUserAdmin):
    form = UserChangeForm
    add_form = SingUpForm
    ordering = ("email",)
    list_display = (
        "email",
        "is_superuser",
    )


admin.site.register(User, UserAmdin)

admin.site.unregister(Group)
