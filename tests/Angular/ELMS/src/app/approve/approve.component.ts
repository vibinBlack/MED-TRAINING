import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SharedService } from '../shared.service';

@Component
({
  selector: 'app-approve',
  templateUrl: './approve.component.html',
  styleUrls: ['./approve.component.css']
})
export class ApproveComponent implements OnInit 
{
  constructor(private service:SharedService,private router:Router) { }
  Leave:any=[];
  filterTerm:any;
  unauth:boolean=false;
  ngOnInit(): void 
  {
    this.getLeave();
  }

  getLeave()
  {    
    this.service.getLeaveList().subscribe(data=>
      {
        this.unauth=true;
        this.Leave=data;
      },
      (error:HttpErrorResponse)=>
      {
        this.unauth=false;
        alert("You are not authorized to view this page");
        this.router.navigate(['home'])
      })
  }

  Change(leaveStatus:any,status:string)
  {
    let object=
    {
      "EmpLeave_Req_ID": leaveStatus.EmpLeave_Req_ID,
      "Emp_FullName": leaveStatus.Emp_FullName,
      "Leave_Type": leaveStatus.Leave_Type,
      "Begin_Date": leaveStatus.Begin_Date,
      "End_Date": leaveStatus.End_Date,
      "Requested_Days": leaveStatus.Requested_Days,
      "Leave_Status": status,
      "Emp_Comments": leaveStatus.Emp_Comments,
      "Emp_No": leaveStatus.Emp_No
    }
    this.service.putLeave(leaveStatus.EmpLeave_Req_ID,object).subscribe(data=>{this.service.getLeaveList().subscribe(data=>{this.Leave=data})});
  }
  
  Status(leaves:any)
  {
    return leaves.Leave_Status=='Pending'
  }

  key:string = 'EmpLeave_Req_ID';
  reverse: boolean=true;
  sort(key:string)
  {
    this.key=key;
    this.reverse=!this.reverse;
  }
}