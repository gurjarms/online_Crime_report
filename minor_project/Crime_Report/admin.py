from django.contrib import admin
from .models import Feedback_table, Fir, tesil


@admin.register(Feedback_table)
class Feedback_register(admin.ModelAdmin):
    list_display = [
        'Full_Name', 'Email', 'Message'
    ]


@admin.register(Fir)
class Fir_register(admin.ModelAdmin):
    list_display = [
        'author', 'Mobile_NO', 'Criminal_name'
    ]


@admin.register(tesil)
class tesil_register(admin.ModelAdmin):
    list_display = [
        'Tehsil', 'author'
    ]
