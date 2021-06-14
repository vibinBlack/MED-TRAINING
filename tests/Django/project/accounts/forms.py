from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
class EmployeeForm(ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['Designation'].empty_label = "Select"
        self.fields['Gender'].empty_label = "please choose value"
        self.fields['Address2'].required = False
        self.fields['Middle_Name'].required = False

class EmpLeaveRequestForm(ModelForm):

    class Meta:
        model=EmpLeaveRequest
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(EmpLeaveRequestForm,self).__init__(*args, **kwargs)
        self.fields['Leave_Status'].required = False

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']