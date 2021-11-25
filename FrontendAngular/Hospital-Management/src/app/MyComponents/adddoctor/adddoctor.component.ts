import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DoctorsService } from 'src/app/Services/doctors.service';

@Component({
  selector: 'app-adddoctor',
  templateUrl: './adddoctor.component.html',
  styleUrls: ['./adddoctor.component.css']
})
export class AdddoctorComponent implements OnInit {
  first_name:string=""
  last_name:string=""
  type:string=""
  dict={}
  temp:any
  isSuperUser:string="no"
  constructor(private api:DoctorsService, private router:Router) { 
    this.temp = sessionStorage.getItem("isSuperUser")
    this.temp != null ? this.isSuperUser = this.temp : this.isSuperUser="no"
  }

  ngOnInit(): void {
  }
  onSubmit = () => {
      this.dict = {'first_name':this.first_name, 'last_name':this.last_name, 'type':this.type}
      this.api.addDoctor(this.dict).subscribe(
        data=>{
          console.log(data)
          this.router.navigate(["/doctors"])
        },
        error=>{
          console.log(error)
        }
      )
  }
}
