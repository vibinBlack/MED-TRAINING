import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Leave } from '../leave';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-apply',
  templateUrl: './apply.component.html',
  styleUrls: ['./apply.component.css']
})
export class ApplyComponent implements OnInit {

  constructor(private service:SharedService,private router:Router) { }

  Leave:any=[];
  employees:any=[];
  ngOnInit(): void {
    this.leaveId(); 
    this.empId();
  }

  empId(){
    this.service.getEmpId().subscribe(data=>{this.employees=data})
  }

  leaveId(){
    this.service.getLeaveId().subscribe(data=>{this.Leave=data})
  }

  LeaveType= new FormControl('', [Validators.required]);
  BeginDate= new FormControl('', [Validators.required]);
  EndDate= new FormControl('', [Validators.required]);
  RequestedDays= new FormControl('', [Validators.required]);
  EmpComments= new FormControl('', [Validators.required]);

  leaveForm = new FormGroup({
    LeaveType: this.LeaveType,
    BeginDate: this.BeginDate,
    EndDate: this.EndDate,
    RequestedDays: this.RequestedDays,
    EmpComments: this.EmpComments
  });  
  onSubmit()
  {    
    let object={
      "Emp_FullName": this.employees.First_Name,
      "Leave_Type": this.leaveForm.get('LeaveType')!.value,
      "Begin_Date": this.leaveForm.get('BeginDate')!.value,
      "End_Date": this.leaveForm.get('EndDate')!.value,
      "Requested_Days": this.leaveForm.get('RequestedDays')!.value,
      "Emp_Comments": this.leaveForm.get('EmpComments')!.value,
      "Emp_No": this.employees.Emp_No
    }
    this.service.postLeave(object).subscribe(data=>{console.log('Success!',data),this.leaveForm.reset(),this.router.navigate(['/apply']);},error=>console.error('Error!',error));
    
    
  }

  Cancel(leaveStatus:any)
  {
    let object={
      "EmpLeave_Req_ID": leaveStatus.EmpLeave_Req_ID,
      "Emp_FullName": leaveStatus.Emp_FullName,
      "Leave_Type": leaveStatus.Leave_Type,
      "Begin_Date": leaveStatus.Begin_Date,
      "End_Date": leaveStatus.End_Date,
      "Requested_Days": leaveStatus.Requested_Days,
      "Leave_Status": "Cancelled",
      "Emp_Comments": leaveStatus.Emp_Comments,
      "Emp_No": leaveStatus.Emp_No
    }
    console.log(object);
    this.service.putLeave(leaveStatus.EmpLeave_Req_ID,object).subscribe(data=>{this.leaveId()})
    
  }
  disable(leaves:any)
  {
    return leaves.Leave_Status!='Pending'
  }
}
