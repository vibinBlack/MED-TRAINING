"""tests"""
from datetime import datetime
import unittest
from django.shortcuts import get_object_or_404
from django.test import Client
from appointments.models import Doctor, Timeslot

class Testing(unittest.TestCase):
    """testing timeslots module"""
    def test_time1(self):
        """test1"""
        # print(self.doctor,self.d,self.obj.slots)
        client = Client()
        doctor = get_object_or_404(Doctor,pk=5)
        date_test = datetime.strptime('oct 26 2021', '%b %d %Y').date()
        client.post('/timeslot/5',{'intime': '10:00', 'outime': '16:00', 'each_slot_time': '00:30', 'break_time':'12:00 13:00','date':'2021-10-26'})
        obj = Timeslot.objects.get(doctor=doctor, date=date_test)
        # print(d)
        self.assertEqual(obj.slots,'10:00,10:30,11:00,11:30,13:00,13:30,14:00,14:30,15:00,15:30,')

    def test_time2(self):
        """test2"""
        client = Client()
        doctor = get_object_or_404(Doctor,pk=4)
        date_test = datetime.strptime('oct 26 2021', '%b %d %Y').date()
        client.post('/timeslot/4',{'intime': '9:00', 'outime': '16:00', 'each_slot_time': '00:45', 'break_time':'11:00 11:30,14:00 14:30','date':'2021-10-26'})
        obj = Timeslot.objects.get(doctor=doctor, date=date_test)
        self.assertEqual(obj.slots,'9:00,9:45,11:30,12:15,13:00,14:30,15:15,')

    def test_time3(self):
        """test3"""
        client = Client()
        doctor = get_object_or_404(Doctor,pk=6)
        date_test = datetime.strptime('oct 26 2021', '%b %d %Y').date()
        client.post('/timeslot/6',{'intime': '9:00', 'outime': '16:00', 'each_slot_time': '00:40', 'break_time':'14:00 15:30','date':'2021-10-26'})
        obj = Timeslot.objects.get(doctor=doctor, date=date_test)
        self.assertEqual(obj.slots,'9:00,9:40,10:20,11:00,11:40,12:20,13:00,')
