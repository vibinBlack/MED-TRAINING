"""registering models"""
from django.contrib import admin
from .models import Doctor, Patient, Appointment
# Register your models here.

admin.site.register(Doctor)
# admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """registering patient model"""
    list_display = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """registering appointment model"""
    list_display = ('date','patient','doctor')
