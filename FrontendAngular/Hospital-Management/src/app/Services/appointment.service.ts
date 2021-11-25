import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppointmentService {

  name: string = "";
  token: string = "";
  header: any;
  temp: any;
  baseurl = 'http://127.0.0.1:8000/appointments/'
  constructor(private http: HttpClient) {



    this.temp = sessionStorage.getItem("token")
    this.temp != null ? this.token = this.temp : ""

    this.header = new HttpHeaders({
      "Authorization": "token " + this.token,
      "Content-Type": "application/json",
    });
  }
  myAppointments(): Observable<any> {
    // console.log(this.token)
    return this.http.get(this.baseurl + 'myappointments/', { 'headers': this.header })
  }
  allAppointments(): Observable<any> {
    // console.log(this.token)
    return this.http.get(this.baseurl + 'allappointments/', { 'headers': this.header })
  }
  deleteAppointment(pk:string): Observable<any> {
    // console.log(this.token)
    return this.http.get(this.baseurl + 'deleteappointment/'+pk, { 'headers': this.header })
  }
  getAppointmentsOnSearch(data:any):Observable<any>{
    return this.http.get(this.baseurl+'appointmentssearch/',{'params':data,'headers':this.header})
  }
  appointmentFilters(data:any):Observable<any>{
    return this.http.get(this.baseurl+'appointmentsfilter/',{'params':data,'headers':this.header})
  }
}
