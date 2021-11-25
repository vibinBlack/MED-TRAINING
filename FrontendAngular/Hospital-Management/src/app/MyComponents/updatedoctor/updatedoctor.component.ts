import { Component, Input, OnInit } from '@angular/core';
import { DoctorsService } from 'src/app/Services/doctors.service';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-updatedoctor',
  templateUrl: './updatedoctor.component.html',
  styleUrls: ['./updatedoctor.component.css']
})
export class UpdatedoctorComponent implements OnInit {

  first_name:string=""
  last_name:string=""
  type:string=""
  dict={}
  id:string=""
  temp:any;
  isSuperUser:string="no"

  constructor(private api:DoctorsService,private route: ActivatedRoute, private router:Router) { 
   const temp = this.route.snapshot.paramMap.get('docId') 
    temp!=null ? this.id=temp : this.id='-1'
    this.temp = sessionStorage.getItem("isSuperUser")
    this.temp != null ? this.isSuperUser = this.temp : this.isSuperUser="no"
  }
    
  ngOnInit(): void {
    
  }

  onUpdate = (pk:string) => {
    
    this.dict = {'first_name':this.first_name, 'last_name':this.last_name, 'type':this.type}
    this.api.updateDoctor(this.dict,pk).subscribe(
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
