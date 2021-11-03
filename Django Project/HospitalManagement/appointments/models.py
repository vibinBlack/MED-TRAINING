from django.db import models

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.type})'

    class Meta:
        permissions = (("modify_doctor", "Modify Doctor"),)


class Patient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Appointment(models.Model):
    patient = models.ForeignKey('Patient',on_delete=models.SET_NULL, null=True,blank=True)
    doctor = models.ForeignKey('Doctor',on_delete=models.SET_NULL, null=True,blank=True)
    date = models.DateField()
    time = models.CharField(max_length=10,null=True)

    def __str__(self):
        return f'{self.patient}'

class Timeslot(models.Model):
    doctor = models.ForeignKey('Doctor',on_delete=models.SET_NULL, null=True,blank=True)
    date = models.DateField()
    slots = models.CharField(max_length=300)    
    eachslottime = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.doctor} {self.date} {self.slots}'
