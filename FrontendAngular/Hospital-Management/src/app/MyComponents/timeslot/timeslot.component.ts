import { Time } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TimeslotService } from 'src/app/Services/timeslot.service';

@Component({
  selector: 'app-timeslot',
  templateUrl: './timeslot.component.html',
  styleUrls: ['./timeslot.component.css']
})
export class TimeslotComponent implements OnInit {
  intime!:Time;
  outime!:Time;
  each_slot_time!:Time;
  break_time!:string;
  date!:Date;
  id:string='-1'
  dict:object = {}
  temp:any;
  isSuperUser:string="no"

  datenow = new Date()

  minDate!:string
  maxDate!:string
  msg:boolean = false

  constructor(private api:TimeslotService,private route: ActivatedRoute,private router:Router) { 
    const temp = this.route.snapshot.paramMap.get('docId') 
    temp!=null ? this.id=temp : this.id='-1'
    this.temp = sessionStorage.getItem("isSuperUser")
    this.temp != null ? this.isSuperUser = this.temp : this.isSuperUser="no"
   
    this.datenow.setDate(this.datenow.getDate()+1)
    this.minDate = this.datenow.toISOString().slice(0, 10)
    console.log(this.minDate);

    this.datenow.setDate(this.datenow.getDate()+7)
    this.maxDate = this.datenow.toISOString().slice(0, 10)
    
  }

  ngOnInit(): void {

    
  }
  onSubmit = () => {
    this.dict = {
      'intime':this.intime,
      'outime':this.outime,
      'each_slot_time':this.each_slot_time,
      'break_time':this.break_time,
      'date':this.date,
    }
    this.api.InputTimeSlots(this.dict,this.id).subscribe(
      data=>{
        console.log(data)
        if(data.failure==="Time Slots Already Exist")
        {
          this.msg = true
        }
        else
        {
          this.router.navigate(['/doctors'])
        }
      },
      error=>{
        console.log(error)
      }
    )
  }
}
