import django_filters
from .models import *
from django_filters import  CharFilter

class EmployeeFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='First_Name', lookup_expr='icontains')
    Email = CharFilter(field_name='Email_Address', lookup_expr='icontains')
    class Meta:
        model=Employee
        fields=['Emp_No', 'Mobile_Number', 'Hire_Date', 'Gender', 'Designation']