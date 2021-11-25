import { Time } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BookingService } from 'src/app/Services/booking.service';

@Component({
  selector: 'app-booking',
  templateUrl: './booking.component.html',
  styleUrls: ['./booking.component.css']
})
export class BookingComponent implements OnInit {

  slots:any[]=[];
  id:string="";
  selectedDate!:Date;
  selectedTimeSlot!:Time;
  AvailableDates:String[]=[];
  TimeSlotsForSelecteddate:String[]=[];
  dict={}
  slotsAvailabe:boolean = false
  msg:string=""
  constructor(private api:BookingService,private route: ActivatedRoute,private router:Router) { 
   const temp = this.route.snapshot.paramMap.get('docId') 
    temp!=null ? this.id=temp : this.id='-1'

    this.api.getTimeSlots(this.id).subscribe(
      data=>{
        console.log(data.all_dates_slots)
        this.slots=data.all_dates_slots
        this.msg = ""
        for(let slot in this.slots)
        {
          console.log(slot)
          this.AvailableDates.push(slot)
          console.log(this.slots[slot])
          for(var time of this.slots[slot]){
            console.log(time)
        }
       }
       if(this.AvailableDates.length!=0)
        this.slotsAvailabe=true
       console.log(this.AvailableDates)
      },
      error=>{
      console.log(error);
      }
    )
  }

  ngOnInit(): void {
  }
  getSlots() {
    console.log(this.selectedDate)
    if(this.selectedDate===undefined)
    {
      this.msg="Please Select Date"
    }
    for(let slot in this.slots)
    {
      if(slot===String(this.selectedDate))
      {
        console.log(this.slots[slot])
        this.TimeSlotsForSelecteddate = this.slots[slot]
      }
    }
  }
  putSlots() {
    this.dict = {'date':this.selectedDate,'time':this.selectedTimeSlot}
    console.log(this.dict)
    this.api.putTimeSlot(this.dict, this.id).subscribe(
      data=>{
        console.log(data)
        if(data.failure !== "Appointment already Exists")
            this.router.navigate(['/myappointments'])
        this.msg=data.failure
      },
      error=>{
        console.log(error)
        this.msg = "Please Select Date"
      }
    )
    
  }
}
