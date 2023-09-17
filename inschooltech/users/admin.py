from config.basemodels import BaseAdminModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin, BaseAdminModel):
    pass


admin.site.register(User, CustomUserAdmin)
