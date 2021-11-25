import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  baseurl = 'http://127.0.0.1:8000/appointments/'

  constructor(private http: HttpClient) { }

    CheckLogin(data:any):Observable<any>{
      const headers = { 'content-type': 'application/json'} 
      const body=JSON.stringify(data);
      // console.log(data)
      // console.log(body)
      return this.http.post(this.baseurl + 'api-token-auth/', body,{'headers':headers})
  }
  checkUserRole(data:any):Observable<any>{
    const headers = { 'content-type': 'application/json'} 
    const body=JSON.stringify(data);
    return this.http.post(this.baseurl + 'login/', body,{'headers':headers})
}
}
