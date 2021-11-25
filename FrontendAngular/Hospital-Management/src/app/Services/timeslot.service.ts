import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TimeslotService {

  name:string="";
  token:string="";
  header:any;
  temp:any;
  baseurl = 'http://127.0.0.1:8000/appointments/timeslot/'

    constructor(private http: HttpClient) {
      
      this.temp = sessionStorage.getItem("token")
      this.temp != null ? this.token = this.temp : ""
  
      this.header = new HttpHeaders({
        "Authorization":"token "+this.token,
        "Content-Type": "application/json",
      });
     }

    InputTimeSlots(data:any,pk:string):Observable<any>{
      // const headers = { 'content-type': 'application/json'} 
      const body=JSON.stringify(data);
      // console.log(data)
      // console.log(body)
      return this.http.post(this.baseurl + pk, body,{'headers':this.header})
  }
}
