from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import jwt, datetime
from django.http import HttpRequest
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from .forms import *
from .filters import *
from .decorators import *
from .serializers import *
# Create your views here.

@unauthenticated_user
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    return render(request,'accounts/register.html', {'form':form})

@unauthenticated_user
def loginPage(request):
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
@allowed_users(allowed_roles=['Employee', 'Manager'])
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
@allowed_users(allowed_roles=['HR', 'Manager'])
def approve(request):
    history=EmpLeaveRequest.objects.all()
    return render(request,'accounts/approve.html',{'history':history})

@login_required(login_url='login')
@allowed_users(allowed_roles=['HR', 'Manager'])
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
@allowed_users(allowed_roles=['HR', 'Manager'])
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
@allowed_users(allowed_roles=['HR', 'Manager'])
def delete(request,Emp_No):
    employees = Employee.objects.get(pk=Emp_No)
    employees.delete()
    return redirect('/edit')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Employee', 'Manager'])
def Cancel(request,EmpLeave_Req_ID):
    employees = EmpLeaveRequest.objects.get(pk=EmpLeave_Req_ID)
    employees.Leave_Status='Cancelled'
    employees.save()
    return redirect('/apply')

@login_required(login_url='login')
@allowed_users(allowed_roles=['HR', 'Manager'])
def accept(request,EmpLeave_Req_ID):
    leave=EmpLeaveRequest.objects.get(pk=EmpLeave_Req_ID)
    leave.Leave_Status='Approved'
    leave.save()
    return redirect("/approve")

@login_required(login_url='login')
@allowed_users(allowed_roles=['HR', 'Manager'])
def decline(request,EmpLeave_Req_ID):
    leave=EmpLeaveRequest.objects.get(pk=EmpLeave_Req_ID)
    leave.Leave_Status='Declined'
    leave.save()
    return redirect("/approve")

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Profile'  :'profile/',
		'Apply':'apply/',
		'Approve':'approve/',
		'Edit':'edit/',
		'Sort':'edit/<int:sort>/',
        'Add':'add/',
        'Update':'add/<int:Emp_No>/',
        'Delete':'edit/delete/<int:Emp_No>/',
        'Cancel':'apply/Cancel/<int:EmpLeave_Req_ID>/',
        'Accept':'accept/<int:EmpLeave_Req_ID>',
        'Decline':'decline/<int:EmpLeave_Req_ID>',
		}
	return Response(api_urls)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['HR', 'Manager'])
def employeeList(request):
    employee = Employee.objects.all().order_by('Emp_No')
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def employeeDetail(request):
    Users=request.user
    email=Users.email
    employee = Employee.objects.get(Email_Address=email)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@allowed_users(allowed_roles=['HR', 'Manager'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def employeeCreate(request):
	serializer = EmployeeSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
@allowed_users(allowed_roles=['HR', 'Manager'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def employeeUpdate(request, id):
	employee = Employee.objects.get(Emp_No=id)
	serializer = EmployeeSerializer(instance=employee, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
@allowed_users(allowed_roles=['HR', 'Manager'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def employeeDelete(request, id):
	employee = Employee.objects.get(Emp_No=id)
	employee.delete()
	return Response('Item succsesfully delete!')
    

@api_view(['GET'])
@allowed_users(allowed_roles=['HR', 'Manager'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def leaveList(request):
	leave = EmpLeaveRequest.objects.all().order_by('EmpLeave_Req_ID')
	serializer = EmpLeaveRequestSerializer(leave, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def leaveDetail(request):
    Users=request.user
    email=Users.email
    employee = Employee.objects.get(Email_Address=email)
    id=employee.Emp_No
    leave = EmpLeaveRequest.objects.filter(Emp_No=id)
    serializer = EmpLeaveRequestSerializer(leave, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def leaveCreate(request):
	serializer = EmpLeaveRequestSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def leaveUpdate(request, id):
	leave = EmpLeaveRequest.objects.get(EmpLeave_Req_ID=id)
	serializer = EmpLeaveRequestSerializer(instance=leave, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
@allowed_users(allowed_roles=['HR', 'Manager'])
def aregister(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@unauthenticated_user
def alogin(request):
    data = request.data
    username = data.get('username', '')
    password = data.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is None:
        raise AuthenticationFailed('Invalid credentials')   
    payload = {
            'id': user.id,
            'email' : user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
    print(token)
    # response = Response()
    # response.set_cookie(key='jwt', value=token, httponly=True)
    #print(response.set_cookie(key='jwt', value=token, httponly=True,samesite='None',secure=True,path='/'))
    # response.data = {
    #     'jwt': token
    # }
    # return response
    return Response({
        'jwt': token
    })

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def auser(request):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def alogout(request):
    token = request.COOKIES.get('jwt')
    print(token)
    response = Response()
    response.delete_cookie('jwt')
    token = request.COOKIES.get('jwt')
    print(token)
    response.data = {
        'message': 'success'
    }
    return response

# @api_view(['POST'])
# def alogout(request, email):
#     user = User.objects.filter(email=email).first()  
#     payload = {
#             'id': user.id,
#             'email' : user.email,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=2),
#             'iat': datetime.datetime.utcnow()
#         }
#     token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
#     print("logout")
#     print(token)
#     response = Response()
#     response.set_cookie(key='jwt', value=token, httponly=True)
#     response.data = {
#         'jwt': token
#     }
#     return response