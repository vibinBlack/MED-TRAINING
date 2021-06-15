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
    employee_list = Employee.objects.get(Email_Address=request.user.email)
    return render(request,'accounts/home.html',{'employees': employee_list})

@login_required(login_url='login')
def profile(request):
    employees=Employee.objects.get(Email_Address=request.user.email)
    return render(request,'accounts/profile.html',{'employees':employees})

@login_required(login_url='login')
def apply(request):
    employees=Employee.objects.get(Email_Address=request.user.email)
    id=employees.Emp_No
    form=EmpLeaveRequestForm()
    if request.method == 'POST':
        form=EmpLeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/apply')
        else:
            print(form.errors)
    history = []
    for e in EmpLeaveRequest.objects.filter(Emp_No=id):
        leaves = {}
        leaves['Emp_No'] = e.Emp_No
        leaves['Leave_Type'] = e.Leave_Type
        leaves['Begin_Date'] = e.Begin_Date.strftime("%Y-%m-%d")
        leaves['End_Date'] = e.End_Date.strftime("%Y-%m-%d")
        leaves['Requested_Days'] = e.Requested_Days
        leaves['Leave_Status'] = e.Leave_Status
        leaves['EmpLeave_Req_ID'] = e.EmpLeave_Req_ID
        if e.Leave_Status == 'Pending':
            leaves['Display'] = 'inline'
        else:
            leaves['Display'] = 'none'

        history.append(leaves)
    return render(request,'accounts/apply.html',{'history':history,'form':form,'id':id})

@login_required(login_url='login')
def approve(request):
    history=EmpLeaveRequest.objects.all()
    return render(request,'accounts/approve.html',{'history':history})

@login_required(login_url='login')
def edit(request,sort=0):
    employees = Employee.objects.all()
    if sort==1:
        employees = Employee.objects.all().order_by('First_Name')
    if sort==2:
        employees = Employee.objects.all().order_by('Gender')
    if sort==3:
        employees = Employee.objects.all().order_by('Mobile_Number')
    if sort==4:
        employees = Employee.objects.all().order_by('Email_Address')
    if sort==5:
        employees = Employee.objects.all().order_by('Designation')
    if sort==6:
        employees = Employee.objects.all().order_by('Hire_Date')
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