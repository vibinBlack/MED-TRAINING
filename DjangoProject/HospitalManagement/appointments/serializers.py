"""serializers"""
from rest_framework import serializers
from .models import Doctor,Patient,Appointment,Timeslot

class DoctorSerializer(serializers.ModelSerializer):
    """doctor serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        """meta"""
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    """patient serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        """meta"""
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    # customefield = Field(source="doctorName")
    """appointment serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        """meta"""
        model = Appointment
        fields = '__all__'

class TimeslotSerializer(serializers.ModelSerializer):
    """timeslot serializer"""
    class Meta:# pylint: disable=too-few-public-methods
        """meta"""
        model = Timeslot
        fields = '__all__'
