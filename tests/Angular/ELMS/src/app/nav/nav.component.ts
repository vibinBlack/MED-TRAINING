import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  constructor(public service:SharedService) { }
  employees:any=[]; 

  ngOnInit(): void {
    this.empId()
  }
  empId()
  {
    this.service.getEmpId().subscribe(data=>{this.employees=data})
  }
  employee()
  {
    console.log('employee')
    return this.employees.Designation!='Employee'
  }

}
