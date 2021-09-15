import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SharedService } from '../shared.service';

@Component
({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.css']
})
export class EmployeesComponent implements OnInit 
{
  constructor(private service:SharedService,private router:Router) { }

  Employee:any=[];
  filterTerm:any;
  p : number = 1;
  unauth:boolean=false;
  empNo:any;

  ngOnInit(): void 
  {
    this.empList();
  }

  empList()
  {
    this.service.getEmpList().subscribe(data=>
      {
        this.unauth=true;
        console.log(this.unauth)
        this.Employee=data
      },
      (error:HttpErrorResponse)=>
      {
        this.unauth=false;
        console.log(this.unauth)
        alert("You are not authorized to view this page");
        this.router.navigate(['home'])
      })
  }

  add()
  {
    this.router.navigateByUrl('edit',{state:this.empNo})
  }
  edit(empNo:any)
  {    
    this.router.navigateByUrl('update',{state:empNo})
  }
  delete(del:any)
  {    
    this.service.delEmp(del.Emp_No).subscribe(data=>{this.empList(),this.router.navigate(['/employees'])})
  }
  // employees:any=[];
  // empId()
  // {
  //   this.service.getEmpId().subscribe(data=>{this.employees=data})
  // }
  // employee()
  // {
  //   console.log(this.employees.Designation)
  //   return this.employees.Designation!='Employee'
  // }

  key:string = 'Emp_No';
  reverse: boolean=true;
  sort(key:string)
  {
    this.key=key;
    this.reverse=!this.reverse;
  }
}