import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProfileService implements CanActivate{

  url ="http://127.0.0.1:8000";
  constructor(private http:HttpClient,private router :Router) {  }
  
  token =sessionStorage.getItem('token')
  headers= new  HttpHeaders().set("Authorization","Token"+" "+this.token)
  
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
    if(this.token!= null){
      return true
    }
      this.router.navigateByUrl('login')
      return false
  }

  public getBooks(){
    return this.http.get(this.url+'/books/',{'headers': this.headers });
  }
  
  public getBookList(val:any){
    return this.http.get(this.url+'/books/'+val,{'headers': this.headers });
  }



  // STUDENT API REQUESTS
  public getStudentList(val:any){
    return this.http.get(this.url+'/students/'+val,{'headers': this.headers });
  }


  // STAFF API REQUESTS

  public getStaffList(val:any){
    return this.http.get(this.url+'/staff/'+val,{'headers': this.headers });
  }

  
  //Student Books API
  public getstudentBorrower(val:any){
    return this.http.get(this.url+'/students-data/'+val,{'headers': this.headers });
  }

  //Staff Books API

  public getstaffBorrower(val:any){
    return this.http.get(this.url+'/staff-data/'+val,{'headers': this.headers });
  }

  public home(){
    return this.http.get(this.url+'/userview',{'headers': this.headers });
  }
}
