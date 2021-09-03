import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { Emitters } from 'src/app/emitters/emitters';


import { StaffService } from 'src/app/SharedServices/staff.service';

@Component({
  selector: 'app-editstaff',
  templateUrl: './editstaff.component.html',
  styleUrls: ['./editstaff.component.css']
})
export class EditstaffComponent implements OnInit {

  constructor(private service:StaffService,private router:Router,private _Activatedroute :ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  @Input()
  id:any;
  staff : any =[];
  formname !: string
  status :boolean = false 
  emp_id =new FormControl('',[Validators.required])
  staff_name = new FormControl('',[Validators.required])

  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.id = params.get('id')
    })
    if (this.id !=0){
    this.service.getStaffList(this.id).subscribe((res:any)=>
    {
      this.emp_id.setValue(res.emp_id),
      this.staff_name.setValue(res.staff_name)
    })
    this.status=false
    this.formname = "Staff Edit Form"
  }
  else {
    this.formname = "Staff Add Form"
    this.status=true
  }
  }
  
  staffform = new FormGroup({
    emp_id : this.emp_id,
    staff_name : this.staff_name
  })
  updateStaff(){
    this.SpinnerService.show()
    this.service.editStaff(this.staffform.value).subscribe(res=>{
      this.SpinnerService.hide();
      this.router.navigate(["staff"]) },
      err=>{
        this.SpinnerService.hide()
      })
  }

  addStaff(){
    this.SpinnerService.show()
    this.service.addStaffs(this.staffform.value).subscribe(res=>{
      this.SpinnerService.hide()
      this.router.navigate(["staff"]) },
      err=>{
        this.SpinnerService.hide();
      })
  }
}
