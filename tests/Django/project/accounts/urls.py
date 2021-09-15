from django.urls import path
from .import views
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

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
    path('accept/<int:EmpLeave_Req_ID>', views.accept,name="accept"),
    path('decline/<int:EmpLeave_Req_ID>', views.decline,name="decline"),
    
    path('api/', views.apiOverview, name="api-overview"),
    path('employee-list/', views.employeeList, name="employee-list"),
	path('employee-detail/', views.employeeDetail, name="employee-detail"),
	path('employee-create', views.employeeCreate, name="employee-create"),
	path('employee-update/<int:id>', views.employeeUpdate, name="employee-update"),
	path('employee-delete/<int:id>', views.employeeDelete, name="employee-delete"),
    
    path('leave-list/', views.leaveList, name="leave-list"),
	path('leave-detail/', views.leaveDetail, name="leave-detail"),
	path('leave-create/', views.leaveCreate, name="leave-create"),
	path('leave-update/<int:id>', views.leaveUpdate, name="leave-update"),
    path('aregister/', views.aregister,name="aregister"),
    path('alogin/', obtain_jwt_token,name="alogin"),
    path('auser/', views.auser,name="auser"),
    path('alogout/', views.alogout,name="alogout"),
]