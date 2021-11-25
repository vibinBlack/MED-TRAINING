import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DoctorsService {
name:string="";
token:string="";
header:any;
temp:any;
  baseurl = 'http://127.0.0.1:8000/appointments/'
  // httpHeaders = new HttpHeaders({'Content-Type':'application/json'});
  constructor(private http: HttpClient) {

    this.temp = sessionStorage.getItem("token")
    this.temp != null ? this.token = this.temp : ""

    this.header = new HttpHeaders({
      "Authorization":"token "+this.token,
      "Content-Type": "application/json",
    });
   }

   getDoctors(): Observable<any>{
      return this.http.get(this.baseurl + 'doctors/', {headers:this.header})
   }

   addDoctor(data:any):Observable<any>{
    const headers = { 'content-type': 'application/json'} 
    const body=JSON.stringify(data);
    console.log(data)
    console.log(body)
    return this.http.post(this.baseurl + 'adddoctor/', body,{'headers':this.header})
   }
   
   deleteDoctor(data:number):Observable<any>{
     return this.http.delete(this.baseurl + 'deletedoctor/'+data, {headers:this.header})
   }

   updateDoctor(data:object,pk:string):Observable<any>{
     const body = JSON.stringify(data)
    return this.http.put(this.baseurl + 'updatedoctor/'+pk,body, {headers:this.header})
  }

  getDoctorName(pk:string):Observable<any>{
    return this.http.get(this.baseurl + 'doctorname/'+pk, {headers:this.header})
  }

  getDoctorsonSearch(data:any):Observable<any>{
    return this.http.get(this.baseurl+'doctorssearch/',{'params':data,'headers':this.header})
  }
   getSpecialization():Observable<any>{
     return this.http.get(this.baseurl+'specialization/',{'headers':this.header})
   }

   doctorFilters(data:any):Observable<any>{
    return this.http.get(this.baseurl+'doctorsfilter/',{'params':data,'headers':this.header})
  }
}
