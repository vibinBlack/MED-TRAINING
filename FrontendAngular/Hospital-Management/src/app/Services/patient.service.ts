import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PatientService {
  name:string="";
  token:string="";
  header:any;
  temp:any;
    baseurl = 'http://127.0.0.1:8000/appointments/'

    constructor(private http: HttpClient) {
 
      this.temp = sessionStorage.getItem("token")
      this.temp != null ? this.token = this.temp : ""
  
      this.header = new HttpHeaders({
        "Authorization":"token "+this.token,
        "Content-Type": "application/json",
      });
     }

    addPatient(data:any):Observable<any>{
      // const headers = { 'content-type': 'application/json'} 
      const body=JSON.stringify(data);
      // console.log(data)
      // console.log(body)
      return this.http.post(this.baseurl + 'addpatient/', body,{'headers':this.header})
  }
    getPatients():Observable<any>{
      return this.http.get(this.baseurl+'patients/',{'headers':this.header})
    }

    getPatientsonSearch(value:string):Observable<any>{
      return this.http.get(this.baseurl+'patients/'+value,{'headers':this.header})
    }
    patientFilters(data:any):Observable<any>{
      console.log(data);
      return this.http.get(this.baseurl+'patientsfilter/',{'params':data,'headers':this.header})
    }

    getLocations():Observable<any>{
      return this.http.get(this.baseurl+'locations/',{'headers':this.header})
    }
}
