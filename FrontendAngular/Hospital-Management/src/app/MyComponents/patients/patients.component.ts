import { Component, OnInit } from '@angular/core';
import { patient } from 'src/app/datamodels';
import { PatientService } from 'src/app/Services/patient.service';

@Component({
  selector: 'app-patients',
  templateUrl: './patients.component.html',
  styleUrls: ['./patients.component.css'],
  providers: [PatientService],
})
export class PatientsComponent implements OnInit {
  patients!:patient[];
  patientSearch:string=""
  // location:string=""
  availableLocations:string[]=[]
  selectedLocation:string=""
  constructor(private api:PatientService) { 
    this.getPatients()
    this.getLocations()
  }

  ngOnInit(): void {
  }

  getPatients(){
    this.api.getPatients().subscribe(
      data=>{
        console.log(data);
        this.patients = data
      },
      error=>{
        console.log(error);
        
      }
    )
  }
  getPatientsOnSearch(){
    this.api.getPatientsonSearch(this.patientSearch).subscribe(
      data=>{
        console.log(data);
        this.patients=data
      },
      error=>{
        console.log(error);
      }
    )
  }

  Filters(){
    const filters:any = {};
    if(this.selectedLocation)
    {
      filters.location = this.selectedLocation
    }
    this.api.patientFilters(filters).subscribe(
      data=>{
        console.log(data);
        this.patients = data
      },
      error=>{
        console.log(error);
        
      }
    )
  }
  getLocations(){
    this.api.getLocations().subscribe(
      data=>{
        console.log(data);
        for(let obj of data)
        {
          this.availableLocations.push(obj.location)
        }
        // this.availableLocations=data
      },
      error=>{
        console.log(error);
        
      }
    )
  }

}
