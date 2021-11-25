"""views for appointments module"""
from datetime import datetime,timedelta

# Create your views here.
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from appointments.serializers import DoctorSerializer,AppointmentSerializer, PatientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Doctor, Patient, Appointment, Timeslot

# @login_required
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctors(request):
    """ returns all doctors """
    # print(request)
    doctor_list = Doctor.objects.all()
    serializer = DoctorSerializer(doctor_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def home(request):
    """ returns count of doctors and patients """
    num_doctors = Doctor.objects.count()
    num_patients = Patient.objects.count()
    return Response({'num_doctors':num_doctors,'num_patients':num_patients})

@api_view(['POST'])
def login(request):
    """ if the user is valid, returns whether he is superuser or not"""
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth.login(request, user)

    # if not Patient.objects.filter(name=username).exists():
    #     obj = Patient(name=username)
    #     obj.save()
    return Response({'isSuperUser':request.user.is_superuser})


# @login_required
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def booking(request,primary_key):
    """ for GET request it will returns all dates with timeslots
    for POST request it will store the user selected date and time in database if not exists"""
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, pk=primary_key)

        # date = datetime.now().date() + timedelta(1)
        # print("In booking",request)
        slot = request.data['time']
        date = request.data['date']
        date = datetime.strptime(date, '%Y-%m-%d').date()

        patient = get_object_or_404(Patient,name=request.user.username)
        # print(patient.name, doctor.first_name,date,slot)
        if Appointment.objects.filter(patient=patient, doctor=doctor,type=doctor.type, date=date).count() > 0:
            return Response({'failure':'Appointment already Exists'})
        obj = Appointment(patient = patient, doctor=doctor,type=doctor.type, date=date,time=slot)
        obj.save()
        appointment = Appointment.objects.filter(id=obj.id)
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)
    #else
    doctor = get_object_or_404(Doctor, pk=primary_key)
    each_date_slots=[]
    all_dates = []
    all_dates_slots = {}
    for i in range(1,8):
        date = datetime.now().date() + timedelta(i)
        if Timeslot.objects.filter(doctor=doctor,date=date).count() == 0:
            continue
        all_dates.append(str(date))
        obj = get_object_or_404(Timeslot,doctor=doctor,date=date)
        time = obj.slots.split(',')
        time = time[0:len(time)-1]
        final_slots=[]
        for each_time in time:
            if Appointment.objects.filter(doctor=doctor,date=date,time=each_time).count() == 0:
                final_slots.append(each_time)
        each_date_slots.append(final_slots)
        all_dates_slots[str(date)] = final_slots
        # print(all_dates_slots)
    return Response({'all_dates_slots':all_dates_slots})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctor(request,primary_key):
    """ returns name of the doctor """
    obj = get_object_or_404(Doctor,id=primary_key)
    doctor_name = obj.first_name + obj.last_name
    return Response(data={'name':doctor_name})

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def get_username(request,primary_key):
    """ returns name of the user """
    obj = get_object_or_404(Patient,id=primary_key)
    username = obj.name
    return Response(data={'name':username})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def myappointments(request):
    """ returns all appoinments of user"""
    patient = get_object_or_404(Patient,name=request.user.username)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date')
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def logout(request):
#     auth.logout(request)
#     messages.info(request, 'Logged out Successfully')
#     return Response(data={'success':'success'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deleteappointment(request,primary_key):
    """ deletes a particular appointment """
    if Appointment.objects.filter(pk=primary_key).count()==1:
        Appointment.objects.filter(pk=primary_key).delete()
        return Response(data={'success':'success'})
    return Response(data={'failure':'Appointment not exist'})

# @login_required
# @permission_required('appointments.modify_doctor')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def deletedoctor(request,primary_key):
    """ deletes doctor """
    obj = get_object_or_404(Doctor,pk=primary_key)
    count = Appointment.objects.filter(doctor=obj,date__gte=datetime.now().date()).count()
    if count==0 :
        Appointment.objects.filter(doctor=obj).delete()
        obj.delete()
        return Response(data={'success':'success'})
    return Response(data={'failure':"Appointments Exist.Can't Delete Doctor"})

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def updatedoctor(request,primary_key):
    """ updates details of doctor """
    if request.method == 'PUT':
        # obj.first_name = request.POST['first_name']
        # obj.last_name = request.POST['last_name']
        # obj.type = request.POST['specialization']
        # obj.save()
        # return redirect('doctor')
        # print(request.data)
        doctor = Doctor.objects.get(pk=primary_key)
        serializer = DoctorSerializer(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'success':'success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    doctor_list = Doctor.objects.filter(pk=primary_key)
    serializer = DoctorSerializer(doctor_list, many=True)
    return Response(data=serializer.data)

# @login_required
# @permission_required('appointments.modify_doctor')
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def adddoctor(request):
    """ adds doctor """
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={'success':'success'})
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def allappointments(request):
    """ returns appointments of every user"""
    appointments = Appointment.objects.order_by('-date')
    serializer = AppointmentSerializer(appointments,many=True)
    return Response(data=serializer.data)

# @login_required
# @permission_required('appointments.modify_doctor')
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def addpatient(request):
    """adds patient"""
    username = request.data['username']
    password = request.data['password']
    mobilenumber = request.data['mobilenumber']
    email = str(request.data['email'])
    location = request.data['location']

    if Patient.objects.filter(name=username).exists() or User.objects.filter(username=username).exists():
        return Response({'failure':'Patient Already Exists'})
    if Patient.objects.filter(mobile_number=mobilenumber).exists():
        return Response({'failure':'Mobile Number Already Exists'})
    if Patient.objects.filter(email=email).exists():
        return Response({'failure':'Email Already Exists'})

    User.objects.create_user(username=username,password=password)
    obj = Patient(name=username,mobile_number=mobilenumber,email=email,location=location.lower())
    obj.save()
    messages.info(request, "Patient Added Successfully")
    return Response({'success':'Patient Added Successfully'})


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def get_all_patients(request):
    """returns all patients"""
    patients_list = Patient.objects.all()
    serializer = PatientSerializer(patients_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def get_patients_on_search(request,value):
    """returns patients based on search keyword"""
    query = Q(name__contains=value) | Q(mobile_number__contains=value) | Q(email__contains=value) | Q(location__contains=value)
    serializer = PatientSerializer(Patient.objects.filter(query),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_locations(request):
    """returns all locations of patients without duplicates"""
    return Response(Patient.objects.values('location').distinct())

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patients_on_filter(request):
    """returns patients based on filters"""
    data = request.GET.get("location")
    query = Q(location__contains=data)
    serializer = PatientSerializer(Patient.objects.filter(query),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def get_doctors_on_search(request):
    """returns doctors based on search keyword"""
    value = request.GET.get("doctorSearch")
    query = Q(first_name__icontains=value)  | Q(last_name__icontains=value) | Q(type__icontains=value)
    serializer = DoctorSerializer(Doctor.objects.filter(query),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specializations(request):
    """returns specializations of all doctors without duplicates"""
    return Response(Doctor.objects.values('type').distinct())

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors_on_filter(request):
    """returns doctors based on filters"""
    data = request.GET.get("specialization")
    query = Q(type__contains=data)
    serializer = DoctorSerializer(Doctor.objects.filter(query),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointments_on_search(request):
    """returns appointments based on search keyword"""
    value = request.GET.get("appointmentsSearch")
    query=Q()
    patient = get_object_or_404(Patient,name=request.user.username).pk
    query = Q(type__icontains=value) | Q(date__icontains=value) | Q(doctor__first_name__icontains=value) | Q(doctor__last_name__icontains=value)
    query &= Q(patient_id=patient)
    # appointments = Appointment.objects.filter(patient=patient).order_by('-date')
    serializer = AppointmentSerializer(Appointment.objects.filter(query).order_by('-date'),many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointments_on_filter(request):
    """returns appointments based on filters"""
    specialization = request.GET.get("specialization")
    doctor = request.GET.get("doctor")
    print(doctor)
    query = Q()
    if specialization:
        query &= Q(type__contains=specialization)
    if doctor:
        doctor = doctor.split('.')
        query &= Q(doctor__first_name__iexact=doctor[0]) | Q(doctor__last_name__iexact=doctor[1])

    patient = get_object_or_404(Patient,name=request.user.username).pk
    query &= Q(patient_id=patient)
    serializer = AppointmentSerializer(Appointment.objects.filter(query),many=True)
    return Response(serializer.data)
