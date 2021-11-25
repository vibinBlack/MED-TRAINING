import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookingService {

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

    getTimeSlots(pk:string):Observable<any>{
      // const headers = { 'content-type': 'application/json'} 
      return this.http.get(this.baseurl+'booking/' + pk,{'headers':this.header})
  }

  putTimeSlot(data:any,pk:string):Observable<any>{
    const body=JSON.stringify(data);
    console.log(body)
    return this.http.post(this.baseurl+'booking/'+pk, body, {'headers':this.header})
  }
}
