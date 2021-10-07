from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('doctors/',views.doctors,name='doctor'),
    path('success/<int:pk>', views.success, name='success'),
    path('myappointments/', views.myappointments, name='myappointments'),
    path('logout/', views.logout, name='logout'),
    path('deleteappointment/<int:pk>', views.deleteappointment, name='deleteappointment'),
    path('deletedoctor/<int:pk>',views.deletedoctor, name='deletedoctor'),
    path('updatedoctor/<int:pk>', views.updatedoctor, name='updatedoctor'),
    path('adddoctor/', views.adddoctor, name='adddoctor'),
    path('allappointments/', views.allappointments, name='allappointments'),
    path('addpatient/',views.addpatient, name='addpatient'),
]
