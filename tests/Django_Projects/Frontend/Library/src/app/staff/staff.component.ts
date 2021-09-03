import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { Emitters } from '../emitters/emitters';
import { HomeService } from '../SharedServices/home.service';
import { StaffService } from '../SharedServices/staff.service';

@Component({
  selector: 'app-staff',
  templateUrl: './staff.component.html',
  styleUrls: ['./staff.component.css']
})
export class StaffComponent implements OnInit {

  constructor(private service:StaffService, private mainservice:HomeService,private router:Router,private SpinnerService: NgxSpinnerService) { }

  Staff:any=[];
  staff_info:any;
  search: any;
  is_superuser : any;
  
  ngOnInit(): void {
    this.retrieveall()
  }

  retrieveall(){
    this.SpinnerService.show()
    this.service.getStaffs().subscribe((res) => {
      this.SpinnerService.hide()
      this.Staff=res;
    },
    err=>{
      this.SpinnerService.hide()
    })
    this.is_superuser = (sessionStorage.getItem('is_superuser') == 'true')
  }

  editStaff(staff_details:any){
    this.router.navigate(["/edit-staff/",staff_details.emp_id])
  }

  addFunct(){
    this.router.navigate(["/edit-staff/",'0'])
  }


  deleteStaff(staff_data:any){
   this.SpinnerService.show();
    this.service.deleteStaff(staff_data.emp_id).subscribe(res=>{
      this.SpinnerService.hide();
      this.retrieveall()},
      err=>{
        this.SpinnerService.hide();
      })
    
  }

  staffStatus(val : any ){
      this.router.navigate(["staff-data/",val.emp_id])
  }

  key : any
  reverse : boolean =false
  sort(key:any){
    this.key = key ;
    this.reverse = !this.reverse;
  }
}
