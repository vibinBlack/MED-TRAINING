import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
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

    userName(pk:string):Observable<any>{
      return this.http.get(this.baseurl + 'username/'+pk, {'headers':this.header})
  }
}
