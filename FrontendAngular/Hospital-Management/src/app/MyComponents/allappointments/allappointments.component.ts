import { Component, OnInit } from '@angular/core';
import { AppointmentService } from 'src/app/Services/appointment.service';
import { appointment } from 'src/app/datamodels';
import { DoctorsService } from 'src/app/Services/doctors.service';
import { UserService } from 'src/app/Services/user.service';

@Component({
  selector: 'app-allappointments',
  templateUrl: './allappointments.component.html',
  styleUrls: ['./allappointments.component.css']
})
export class AllappointmentsComponent implements OnInit {

  appointments!:appointment[]
  doctorName:string=""
  constructor(private api:AppointmentService, private api2:DoctorsService, private api3:UserService) {
    this.getAllAppointments()
   }

  ngOnInit(): void {
  }

  getAllAppointments = () => {
    this.api.allAppointments().subscribe(
      data=>{
        console.log(data)
        for(let appointments of data)
        {
          this.api2.getDoctorName(appointments.doctor).subscribe(
            data=>{
              appointments.doctor =  data["name"]
            },
            error =>{
              console.log(error)
            }
          )

          this.api3.userName(appointments.patient).subscribe(
            data=>{
              console.log(data)
              appointments.patient = data["name"]
            },
            error=>{
              console.log(error)
            }
          )
        }
        this.appointments=data
        console.log(data)
      },
      error=>{
        console.log(error)
      }
    )
  }
  getDoctor = (pk:string) => {
    this.api2.getDoctorName(pk).subscribe(
      data=>{
        this.doctorName = data["name"]
        console.log(this.doctorName)
      },
      error =>{
        console.log(error)
      }
    )
  
  }
}
