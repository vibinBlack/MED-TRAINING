from django.shortcuts import render

# Create your views here.
from .models import Doctor, Patient, Appointment, Timeslot
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime,timedelta
from django.contrib.auth.decorators import login_required, permission_required
# class DoctorListView(LoginRequiredMixin, generic.ListView):
#     model = Doctor

@login_required
def doctors(request):
    doctor_list = Doctor.objects.all()
    date = datetime.now().date() + timedelta(1)
    return render(request,'doctor_list.html',{'doctor_list':doctor_list, 'date':date})

def home(request):
    num_doctors = Doctor.objects.count()
    num_patients = Patient.objects.count()
    return render(request,'home.html', {'num_doctors':num_doctors, 'num_patients': num_patients})

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = user_name,password=password)
        if user is not None:
            auth.login(request, user)
            if not Patient.objects.filter(name=user_name).exists():
                obj = Patient(name=user_name)
                obj.save()
            return redirect('doctor')
        else:
            messages.info(request, 'Incorrect Username or Password!!!')
            return redirect('login')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'login.html')

@login_required
def booking(request,pk):

    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, pk=pk)
        # date = datetime.now().date() + timedelta(1)
        slot = request.POST['time']
        date = request.POST['date']
        # print(slot,date)
        patient = get_object_or_404(Patient,name=request.user.username)
        msg = None
        if Appointment.objects.filter(patient=patient, doctor=doctor, date=date).count() > 0:
            msg= 'Appointment already Exists'
        else:
            obj = Appointment(patient = patient, doctor=doctor, date=date,time=slot)
            obj.save()
            # obj = Availability(doctor=doctor,date=date,time=slot,available=False)
            # obj.save()
        return render(request, 'success.html',{'patient_name':patient.name, 'type':doctor.type, 'doctor_name':doctor.first_name+' '+doctor.last_name, 'date':date,'time':slot, 'msg':msg})
    else:
        doctor = get_object_or_404(Doctor, pk=pk)
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
            for t in time:
                if Appointment.objects.filter(doctor=doctor,date=date,time=t).count() == 0:
                    final_slots.append(t)
            each_date_slots.append(final_slots)
            all_dates_slots[str(date)] = final_slots
            # print(all_dates_slots)
    return render(request,'booking.html',{'each_date_slots':each_date_slots, 'all_dates':all_dates,'all_dates_slots':all_dates_slots})

@login_required
def myappointments(request):
    patient = get_object_or_404(Patient,name=request.user.username)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date')

    return render(request, 'myappointments.html',{'appointments':appointments})

def logout(request):
    auth.logout(request)
    messages.info(request, 'Logged out Successfully')
    return redirect('login')

@login_required
def deleteappointment(request,pk):
    # print(time)
    Appointment.objects.filter(pk=pk).delete()
    return redirect('myappointments')

@login_required
@permission_required('appointments.modify_doctor')
def deletedoctor(request,pk):
    # obj = get_object_or_404(Doctor,pk=pk)
    # Appointment.objects.filter(doctor=obj).delete()
    # obj.delete()
    # return redirect('doctor')

    obj = get_object_or_404(Doctor,pk=pk)
    c = Appointment.objects.filter(doctor=obj,date__gte=datetime.now().date()).count()
    if(c==0):
        Appointment.objects.filter(doctor=obj).delete()
        obj.delete()  
    else:
        messages.info(request,"Appointments Exist.Can't Delete Doctor")
    return redirect('doctor')
        

@login_required
@permission_required('appointments.modify_doctor')
def updatedoctor(request,pk):
    obj = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        obj.first_name = request.POST['first_name']
        obj.last_name = request.POST['last_name']
        obj.type = request.POST['specialization']
        obj.save()

        return redirect('doctor')
    else:
        return render(request,'update_doctor.html',{'first_name':obj.first_name, 'last_name':obj.last_name, 'specialization':obj.type})
        
@login_required
@permission_required('appointments.modify_doctor')
def adddoctor(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        specialization = request.POST['specialization']
        Doctor.objects.create(first_name=first_name, last_name=last_name, type=specialization)
        return redirect('doctor')
    else:
        return render(request,'add_doctor.html')

@login_required
@permission_required('appointments.modify_doctor')
def allappointments(request):
    appointments = Appointment.objects.order_by('-date')
    return render(request, 'allappointments.html',{'appointments': appointments})

@login_required
@permission_required('appointments.modify_doctor')
def addpatient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Patient Already Exists")
        else:
            User.objects.create_user(username=username,password=password)
            messages.info(request, "Patient Added Successfully")
        return redirect('addpatient')
    else:
        return render(request, 'addpatient.html')

