from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User  # ایمپورت جدول دیتابیس user

from .models import Profile


# Register your models here.

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton:
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


# :ساخت پروفایل جدید یوزر
class ExtendedProfileAdmin(UserAdmin):
    inlines = (ProfileInLine,)


# Re-register UserAdmin:
admin.site.unregister(User)
admin.site.register(User, ExtendedProfileAdmin)
