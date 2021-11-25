""" views of timeslot module """
# from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from appointments.models import Timeslot,Doctor

# Create your views here.
def hourtomin(hour):
    """converts hour to minutes"""
    hour = hour.split(':')
    minimum = (int(hour[0])*60) + int(hour[1])
    return minimum

def mintohour(minimum):
    """converts minutes to hours"""
    hour = str(int(minimum)//60)
    rem = int(minimum)%60
    hour = hour+ ':' + str(rem)
    if rem==0:
        hour+='0'
    return hour

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def slots(request,primary_key):
    """retuns timeslot for a day based on doctor's intime,outime,slotime,breaks"""
    intime = str(request.data['intime'])
    outime = str(request.data['outime'])
    each_slot_time = str(request.data['each_slot_time'])
    date = request.data['date']
    intime = hourtomin(intime)
    outime = hourtomin(outime)
    each_slot_time = hourtomin(each_slot_time)
    breaks = request.data['break_time'].strip()
    breaks = breaks.split(',')
    doctor = get_object_or_404(Doctor, pk=primary_key)

    if Timeslot.objects.filter(doctor=doctor,date=date).count() >0 :
        return Response({"failure":"Time Slots Already Exist"})

    arr = [0]*1441
    cumulative_sum = [0]*1441
    cumulative_sum[0] = 1
    available_slots = []
    slots_str=''
    slots_24=''
    for i in range(intime,outime+1):
        arr[i]=1
    for i in breaks:
        i = i.split()
        i[0] = hourtomin(i[0].strip())
        i[1] = hourtomin(i[1].strip())
        for j in range(int(i[0]),int(i[1])+1):
            arr[j]=0

    for i in range(intime,outime+1):
        if i != 0:
            cumulative_sum[i]= cumulative_sum[i-1] + arr[i]

    i=intime
    while i<=outime:
        if (arr[i]!=0 and cumulative_sum[i+each_slot_time]-cumulative_sum[i] == each_slot_time) or (i+each_slot_time-1>=0 and arr[i+each_slot_time]==0 and arr[i+each_slot_time-1]!=0 and cumulative_sum[i+each_slot_time]-cumulative_sum[i]+1 == each_slot_time) or (i+1<=outime and arr[i]==0 and arr[i+1]!=0 and cumulative_sum[i+each_slot_time]-cumulative_sum[i] == each_slot_time):
            available_slots.append([i,i+each_slot_time])
            slots_str=slots_str+str(i)+','
            slots_24+= mintohour(i)+','
            i=i+each_slot_time
        else:
            i+=1

    Timeslot.objects.create(doctor=doctor,date=date,slots=slots_24,eachslottime=each_slot_time)
    return Response({'success':'success'})
