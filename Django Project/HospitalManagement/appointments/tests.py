from django.shortcuts import get_object_or_404
from django.test import TestCase

# Create your tests here.
from django.test import Client
from appointments.models import Doctor, Timeslot
from datetime import datetime, time
import unittest

class Testing(unittest.TestCase):
    

    def test_time1(self):
        # print(self.doctor,self.d,self.obj.slots)
        c = Client()
        doctor = get_object_or_404(Doctor,pk=5)
        # print(c.post('/timeslot/<int:pk>', {'intime': '10:00', 'outime': '16:00', 'each_slot_time':'00:30', 'break_time':'12:00 13:00','date':'26/10/2021'}))
        d = datetime.strptime('oct 26 2021', '%b %d %Y').date()
        c.post('/timeslot/5',{'intime': '10:00', 'outime': '16:00', 'each_slot_time': '00:30', 'break_time':'12:00 13:00','date':'2021-10-26'})
        obj = Timeslot.objects.get(doctor=doctor, date=d)
        # print(d)
        # obj = get_object_or_404(Timeslot,doctor=self.doctor,date=d)
        self.assertEqual(obj.slots,'10:00,10:30,11:00,11:30,13:00,13:30,14:00,14:30,15:00,15:30,')

    def test_time2(self):
        c = Client()
        doctor = get_object_or_404(Doctor,pk=4)
        d = datetime.strptime('oct 26 2021', '%b %d %Y').date()
        c.post('/timeslot/4',{'intime': '9:00', 'outime': '16:00', 'each_slot_time': '00:45', 'break_time':'11:00 11:30,14:00 14:30','date':'2021-10-26'})
        obj = Timeslot.objects.get(doctor=doctor, date=d)
        self.assertEqual(obj.slots,'9:00,9:45,11:30,12:15,13:00,14:30,15:15,')

    def test_time3(self):
        c = Client()
        doctor = get_object_or_404(Doctor,pk=6)
        d = datetime.strptime('oct 26 2021', '%b %d %Y').date()
        c.post('/timeslot/6',{'intime': '9:00', 'outime': '16:00', 'each_slot_time': '00:40', 'break_time':'14:00 15:30','date':'2021-10-26'})
        obj = Timeslot.objects.get(doctor=doctor, date=d)
        self.assertEqual(obj.slots,'9:00,9:40,10:20,11:00,11:40,12:20,13:00,')        
