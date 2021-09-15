import { Component } from '@angular/core';
import { SharedService } from './shared.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(public  service:SharedService) { }
  title = 'ELMS';
  employees:any=[]; 

  ngOnInit(): void 
  {
  }
  employee()
  {
    return this.service.getDesignation() !='Employee'
  }
  hr()
  {
    return this.employees.Designation!='HR'
  }
}
