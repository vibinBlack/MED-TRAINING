import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppointmentService } from 'src/app/Services/appointment.service';
import { appointment, doctor } from 'src/app/datamodels';
import { DoctorsService } from 'src/app/Services/doctors.service';
@Component({
  selector: 'app-myappointments',
  templateUrl: './myappointments.component.html',
  styleUrls: ['./myappointments.component.css'],
  providers: [AppointmentService,DoctorsService]
})
export class MyappointmentsComponent implements OnInit {

  appointmentsExist:boolean=false
  appointments!:appointment[]
  appointmentsSearch:string=""
  availableSpecializations:string[] = []
  selectedSpecialization:string=""
  // availableDoctors:string[] = []
  selectedDoctor:string=""
  availableDoctors:doctor[]=[]
  constructor(private api:AppointmentService, private api2:DoctorsService,private router: Router) {
    this.getSpecializations()
    this.getDoctors()
   }

  ngOnInit(): void {
    this.getMyAppointments()
  }

  getMyAppointments() {
    this.api.myAppointments().subscribe(
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
        }
        this.appointments=data
        console.log(data)
        if(this.appointments.length!==0)
        {
          this.appointmentsExist = true
        }
      },
      error=>{
        console.log(error)
      }
    )
  }

  deleteAppointment = (key:number) => {
    let pk=String(key)
    this.api.deleteAppointment(pk).subscribe(
      data=>{
        console.log(data)
        if(data.success === "success")
        {
          console.log("inside")
          this.router.navigate(["/"])
        }
      },
      error=>{
        console.log(error)
      }
    )
  }
  getAppointmentsOnSearch() {
    const search:any = {}
    search.appointmentsSearch = this.appointmentsSearch
    this.api.getAppointmentsOnSearch(search).subscribe(
      data=>{
        console.log(data);
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
        }
        this.appointments=data
      },
      error=>{
        console.log(error);
      }
    )
  }
  getSpecializations() {
    this.api2.getSpecialization().subscribe(
      data=>{
        for(let obj of data)
        {
          this.availableSpecializations.push(obj.type)
        }
      },
      error=>{
        console.log(error);
        
      }
    )
  }
  getDoctors = () => {
    this.api2.getDoctors().subscribe(
      data=> {
        this.availableDoctors=data
        // console.log(this.doctors)
      },
      error =>{
        console.log(error)
      }
    )
  }

  Filters(){
    const filters:any = {};
    if(this.selectedSpecialization)
    {
      filters.specialization = this.selectedSpecialization
    }
    if(this.selectedDoctor)
    {
      filters.doctor = this.selectedDoctor
    }
    this.api.appointmentFilters(filters).subscribe(
      data=>{
        console.log(data);
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
        }
        this.appointments = data
      },
      error=>{
        console.log(error);
      }
    )
  }
}
