from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from appointments.models import Timeslot,Doctor
from datetime import datetime,timedelta
from django.contrib import messages

# Create your views here.
def hourtomin(hour):
    hour = hour.split(':')
    min = (int(hour[0])*60) + int(hour[1])
    return min

def mintohour(min):
    hour = str(int(min)//60)
    rem = int(min)%60
    hour = hour+ ':' + str(rem)
    if rem==0:
        hour+='0'
    return hour

def slots(request,pk):
    # intime,outime,each_slot_time,breaks
    if request.method == 'POST':
        intime = str(request.POST['intime'])
        outime = str(request.POST['outime'])
        each_slot_time = str(request.POST['each_slot_time'])
        date = request.POST['date']
        # print(type(date))
        
        intime = hourtomin(intime)
        outime = hourtomin(outime)
        each_slot_time = hourtomin(each_slot_time)

        breaks = request.POST['break_time'].strip()
        # print(type(breaks)) #str
        breaks = breaks.split(',')
        doctor = get_object_or_404(Doctor, pk=pk)

        if Timeslot.objects.filter(doctor=doctor,date=date).count() >0 :
            messages.info(request,"Time Slots Already Exist")
            min = str(datetime.now().date() + timedelta(1))
            max = str(datetime.now().date() + timedelta(8)) 
            # print(min,max)
            return render(request,'time.html',{'min_date':min, 'max_date':max})

        # breaks = [[630,700],[750,760]]
        arr = [0]*1441
        cs = [0]*1441
        cs[0] = 1
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
                cs[i]= cs[i-1] + arr[i]
        
        i=intime
        while i<=outime:
            if (arr[i]!=0 and cs[i+each_slot_time]-cs[i] == each_slot_time) or (i+each_slot_time-1>=0 and arr[i+each_slot_time]==0 and arr[i+each_slot_time-1]!=0 and cs[i+each_slot_time]-cs[i]+1 == each_slot_time) or (i+1<=outime and arr[i]==0 and arr[i+1]!=0 and cs[i+each_slot_time]-cs[i] == each_slot_time):
                available_slots.append([i,i+each_slot_time])
                slots_str=slots_str+str(i)+','
                slots_24+= mintohour(i)+','
                i=i+each_slot_time
            else:
                i+=1
        # print(slots_str)
        
        # date = datetime.now().date() + timedelta(1)
        Timeslot.objects.create(doctor=doctor,date=date,slots=slots_24,eachslottime=each_slot_time)

        return render(request,'time.html',{'available_slots':available_slots,'all_slots':slots_str,'slots_24':slots_24})
    else:
        min = str(datetime.now().date() + timedelta(1))
        max = str(datetime.now().date() + timedelta(8)) 
        # print(min,max)
        return render(request,'time.html',{'min_date':min, 'max_date':max})