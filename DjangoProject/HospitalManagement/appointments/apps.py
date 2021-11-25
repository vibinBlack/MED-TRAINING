"""apps"""
from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    """configuring appointments module"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments'
