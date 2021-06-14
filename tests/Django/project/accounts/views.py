from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *
from .filters import *
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')		
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        return render(request,'accounts/register.html', {'form':form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password Is Incorrect')
        
        return render(request,'accounts/login.html')

def logoutPage(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'accounts/home.html')

@login_required(login_url='login')
def profile(request):
    employees=Employee.objects.all()

    return render(request,'accounts/profile.html',{'employees':employees})

@login_required(login_url='login')
def apply(request):
    history=EmpLeaveRequest.objects.all()
    form=EmpLeaveRequestForm()
    if request.method == 'POST':
        form=EmpLeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/apply')
        else:
            print(form.errors)
    return render(request,'accounts/apply.html',{'history':history,'form':form})

@login_required(login_url='login')
def approve(request):
    history=EmpLeaveRequest.objects.all()
    return render(request,'accounts/approve.html',{'history':history})

@login_required(login_url='login')
def edit(request):
    employees = Employee.objects.all()

    myFilter=EmployeeFilter(request.GET, queryset=employees)
    employees=myFilter.qs

    return render(request,'accounts/edit.html',{'employees':employees,'myFilter':myFilter})

@login_required(login_url='login')
def add(request,Emp_No=0):
    if request.method == 'GET':
        if Emp_No==0:
            form = EmployeeForm()
        else:
            employees = Employee.objects.get(pk=Emp_No)
            form = EmployeeForm(instance=employees)
        return render(request,'accounts/add.html',{'form': form})
    else:
        if Emp_No == 0:
            form = EmployeeForm(request.POST)
        else:
            employees = Employee.objects.get(pk=Emp_No)
            form = EmployeeForm(request.POST,instance= employees)
        #print('Printing Post:',request.POST)
        if form.is_valid():
            form.save()
        return redirect('/edit')

@login_required(login_url='login')
def delete(request,Emp_No):
    employees = Employee.objects.get(pk=Emp_No)
    employees.delete()
    return redirect('/edit')

@login_required(login_url='login')
def Cancel(request,EmpLeave_Req_ID):
    employees = EmpLeaveRequest.objects.get(pk=EmpLeave_Req_ID)
    employees.delete()
    return redirect('/apply')