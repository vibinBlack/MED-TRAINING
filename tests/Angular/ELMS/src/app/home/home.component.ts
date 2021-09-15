import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component
({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit 
{
  constructor(private service:SharedService) { }
  employees:any=[];
  ngOnInit(): void 
  {    
    this.service.getEmpId().subscribe(data=>
      {
        this.employees=data;
        this.service.setDesignation(this.employees.Designation);
      })
    // setTimeout(()=>{console.log(this.employees.Designation);},100)
    // setTimeout(()=>{this.service.setDesignation(this.employees.Designation);},100)
  }
}