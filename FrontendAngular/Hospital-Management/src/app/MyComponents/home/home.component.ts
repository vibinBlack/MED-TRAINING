import { Component, OnInit } from '@angular/core';
import { HomeService } from 'src/app/Services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [HomeService]
})
export class HomeComponent implements OnInit {
  doctors_count:number=0
  patients_count:number=0

  constructor(private api:HomeService) { 
    this.getCount();
    // console.log(localStorage.getItem('0'))

  }

  ngOnInit(): void {
  }
  getCount = () => {
    this.api.getAllCount().subscribe(
      data => {
        this.doctors_count = data.num_doctors
        this.patients_count = data.num_patients
      },
      error => {
        console.log(error)
      }
    )
  }
}
