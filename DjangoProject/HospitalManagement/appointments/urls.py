"""urls"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from appointments.slots import views as v
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('doctors/',views.doctors,name='doctor'),
    # path('success/<int:primary_key>', views.success, name='success'),
    path('myappointments/', views.myappointments, name='myappointments'),
    # path('logout/', views.logout, name='logout'),
    path('deleteappointment/<int:primary_key>', views.deleteappointment, name='deleteappointment'),
    path('deletedoctor/<int:primary_key>',views.deletedoctor, name='deletedoctor'),
    path('updatedoctor/<int:primary_key>', views.updatedoctor, name='updatedoctor'),
    path('adddoctor/', views.adddoctor, name='adddoctor'),
    path('allappointments/', views.allappointments, name='allappointments'),
    path('addpatient/',views.addpatient, name='addpatient'),
    path('booking/<int:primary_key>',views.booking, name='booking'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('doctorname/<int:primary_key>',views.get_doctor, name='getdoctor'),
    path('username/<int:primary_key>',views.get_username, name='getuser'),
    path('patients/',views.get_all_patients,name="allpatients"),
    path('patients/<str:value>',views.get_patients_on_search,name="patientssearch"),
    path('locations/',views.get_locations,name="locations"),
    path('patientsfilter/',views.get_patients_on_filter,name="patientfilter"),
    path('doctorssearch/',views.get_doctors_on_search,name="patientssearch"),
    path('specialization/',views.get_specializations,name="specializarion"),
    path('doctorsfilter/',views.get_doctors_on_filter,name="doctorfilter"),
    path('appointmentssearch/',views.get_appointments_on_search,name="appointmentssearch"),
    path('appointmentsfilter/',views.get_appointments_on_filter,name="appointmentssearch"),
    path('timeslot/<int:primary_key>',v.slots, name='slots'),

]
