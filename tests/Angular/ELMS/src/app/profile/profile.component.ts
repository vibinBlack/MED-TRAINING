import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component
({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit 
{
  constructor(private service:SharedService) { }
  employees:any=[];
  
  ngOnInit(): void 
  {
    this.empId();
  }

  empId()
  {
    this.service.getEmpId().subscribe(data=>{this.employees=data})
  }
}