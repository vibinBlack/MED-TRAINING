import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders } from '@angular/common/http';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { Emitters } from '../emitters/emitters';
import {Url} from './urls';

@Injectable({
  providedIn: 'root'
})
export class AuthService implements CanActivate{

  // url = "http://127.0.0.1:8000";

  // is_superuser : any;
 
  constructor(private http:HttpClient,private router : Router) { }
  token =sessionStorage.getItem('token')
  headers= new  HttpHeaders().set("Authorization","Token"+" "+this.token)
  is_superuser = (sessionStorage.getItem('is_superuser') == 'true')

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
    this.is_superuser = (sessionStorage.getItem('is_superuser') == 'true')
    this.token=sessionStorage.getItem('token')
    this.headers=this.headers.set("Authorization","Token"+" "+this.token)
    if(this.is_superuser){
      return true
    }
    this.router.navigate(['home'])
    return false
  }
  
  public register(user:any){
    return this.http.post(Url.registerUrl,user,{"headers":this.headers});
  }
  // public getstatus(val:boolean){
  //   this.is_superuser=val;
  // }
}
