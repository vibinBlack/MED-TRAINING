import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PatientService } from 'src/app/Services/patient.service';

@Component({
  selector: 'app-addpatient',
  templateUrl: './addpatient.component.html',
  styleUrls: ['./addpatient.component.css']
})
export class AddpatientComponent implements OnInit {

  username:string=""
  password:string=""
  mobilenumber:string=""
  email:string=""
  location:string=""
  temp:any;
  isSuperUser:string = "no"
  dict={}
  msg:string=""
  constructor(private api:PatientService,private router:Router) { 
    this.temp = sessionStorage.getItem("isSuperUser")
    this.temp != null ? this.isSuperUser = this.temp : this.isSuperUser="no"
  }

  ngOnInit(): void {
  }
  onSubmit = ()=> {
  this.dict = {'username':this.username, 'password':this.password, 'mobilenumber':this.mobilenumber,'email':this.email,'location':this.location}
  this.api.addPatient(this.dict).subscribe(
    data=>{
      console.log(data)
      if(data.failure)
        this.msg= data.failure
      else
        this.router.navigate(["/patients"])
    },
    error=>{
      console.log(error)
    }
  )
  }
}
