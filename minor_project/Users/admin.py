from django.contrib import admin

# Register your models here.
from .models import UserVarify, Profile, UserMobileNo


@admin.register(UserVarify)
class NumberRegister(admin.ModelAdmin):
    list_display = [
        'id', 'mobile'
    ]


@admin.register(Profile)
class ProfileRegister(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'image'
    ]


@admin.register(UserMobileNo)
class usermobileregister(admin.ModelAdmin):
    list_display = [
        'id', 'Mobile', 'user'
    ]
