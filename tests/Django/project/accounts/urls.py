from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('',views.home, name="home"),
    path('profile/',views.profile, name="profile"),
    path('apply/',views.apply, name="apply"),
    path('approve/',views.approve, name="approve"),
    path('edit/',views.edit, name="edit"),
    path('edit/<int:sort>/',views.edit, name="Sort"),
    path('add/',views.add, name="add"),
    path('add/<int:Emp_No>/',views.add, name="update"),
    path('edit/delete/<int:Emp_No>/',views.delete, name="delete"),
    path('apply/Cancel/<int:EmpLeave_Req_ID>/',views.Cancel, name="Cancel"),
]