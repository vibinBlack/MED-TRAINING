import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Employee } from './employee';
import { Leave } from './leave';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Injectable
({
  providedIn: 'root'
})

export class SharedService implements CanActivate
{

  readonly APIUrl = "http://127.0.0.1:8000"

  head = new HttpHeaders().set(
    'Authorization','JWT '+sessionStorage.getItem('jwt')
  )

  constructor(private http:HttpClient,private router:Router, private cookieService: CookieService) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree
  {
    this.head=this.head.set('Authorization','JWT '+sessionStorage.getItem('jwt'))
    if(this.isUserLogedIn())
    {
      return true;
    }
    this.router.navigate(['']);
    return false;
  }

  getEmpList():Observable<Employee[]>
  {
    return this.http.get<Employee[]>(this.APIUrl + '/employee-list/', {headers:this.head});
  }

  putEmp(id:number,data:Employee)
  {
    return this.http.put(this.APIUrl + '/employee-update/'+id,data, {headers:this.head});
  }

  postEmp(empData:Employee):Observable<void>
  {
    return this.http.post<void>(`${this.APIUrl}/employee-create`,empData, {headers:this.head});
  }

  getEmpId():Observable<Employee[]>
  {
    return this.http.get<Employee[]>(this.APIUrl + '/employee-detail/', {headers:this.head});
  }

  delEmp(id:number)
  {
    return this.http.delete(this.APIUrl + '/employee-delete/'+id, {headers:this.head});
  }
  

  getLeaveList():Observable<Leave[]>
  {
    return this.http.get<Leave[]>(this.APIUrl + '/leave-list/', {headers:this.head});
  }
  
  getLeaveId():Observable<Leave[]>
  {
    return this.http.get<Leave[]>(this.APIUrl + '/leave-detail/', {headers:this.head});
  }

  postLeave(val:Leave):Observable<void>
  {
    return this.http.post<void>(this.APIUrl + '/leave-create/',val, {headers:this.head});
  }

  putLeave(id:number,data:Leave)
  { 
    return this.http.put(this.APIUrl + '/leave-update/'+id,data, {headers:this.head});
  }

  postRegister(data:any):Observable<any>
  {
    return this.http.post(this.APIUrl + '/aregister/',data, {headers:this.head});
  }

  postLogin(data:any):Observable<any>
  {
    return this.http.post(this.APIUrl + '/alogin/',data);
  }

  aLogout()
  {
    sessionStorage.removeItem('jwt');
    this.router.navigate([''])
    //return this.http.post(this.APIUrl + '/alogout/', {headers:this.head});
  }

  public isUserLogedIn()
  {
    let login=sessionStorage.getItem('jwt');
    if(login==null)
    {
      return false;
    }
    else
    {
      return true;
    }
  }
  designation!: any;
  setDesignation(data:any)
  {
    console.log(data)
    this.designation=data;
  }
  getDesignation()
  {
    return this.designation;
  }
}