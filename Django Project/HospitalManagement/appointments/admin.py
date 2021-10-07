from django.contrib import admin
from .models import Doctor, Patient, Appointment
# Register your models here.

admin.site.register(Doctor)
# admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date','patient','doctor')
