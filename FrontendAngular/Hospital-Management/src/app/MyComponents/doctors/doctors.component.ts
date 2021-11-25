import { Component, OnInit } from '@angular/core';
import { DoctorsService } from 'src/app/Services/doctors.service';
import { doctor } from 'src/app/datamodels';
import { Router } from '@angular/router';
@Component({
  selector: 'app-doctors',
  templateUrl: './doctors.component.html',
  styleUrls: ['./doctors.component.css'],
  providers: [DoctorsService]
})
export class DoctorsComponent implements OnInit {

  id:number=-1
  doctors:doctor[]=[]
  isSuperUser:string = "no"
  doctorSearch:string=""
  availableSpecializations:string[] = []
  selectedSpecialization:string=""
  temp:any;
  constructor(private api:DoctorsService,private router:Router) {
    this.getDoctors();
    this.getSpecializations();
    this.temp = sessionStorage.getItem("isSuperUser")
    this.temp != null ? this.isSuperUser = this.temp : this.isSuperUser="no"
   }

  ngOnInit(): void {
  }
  getDoctors = () => {
    this.api.getDoctors().subscribe(
      data=> {
        this.doctors=data
        // console.log(this.doctors)
      },
      error =>{
        console.log(error)
      }
    )
  }
  deleteDoctor = (pk:number) => {
    console.log(pk)
    this.api.deleteDoctor(pk).subscribe(
      data=> {
        console.log(data)
        this.router.navigate(["/"])
      },
      error => {
        console.log(error)
      }
    )
  }
  getDoctorsOnSearch(){
    const search:any = {}
    search.doctorSearch = this.doctorSearch
    this.api.getDoctorsonSearch(search).subscribe(
      data=>{
        console.log(data);
        this.doctors=data
      },
      error=>{
        console.log(error);
      }
    )
  }

  getSpecializations() {
    this.api.getSpecialization().subscribe(
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
  Filters(){
    const filters:any = {};
    if(this.selectedSpecialization)
    {
      filters.specialization = this.selectedSpecialization
    }
    this.api.doctorFilters(filters).subscribe(
      data=>{
        console.log(data);
        this.doctors = data
      },
      error=>{
        console.log(error);
      }
    )
  }
}
