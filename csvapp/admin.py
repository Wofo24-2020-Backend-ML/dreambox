from django.contrib import admin
from .models import CSVData


@admin.register(CSVData)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['symbole','date']