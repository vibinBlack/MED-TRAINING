import { HttpClient, HttpClientModule, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Router, RouterStateSnapshot,CanActivate, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { Emitters } from '../emitters/emitters';
import  {Url} from './urls'

@Injectable({
  providedIn: 'root'
})
export class HomeService implements CanActivate{

  constructor(private router : Router,private http:HttpClient) { }

  is_superuser : any;
  token=sessionStorage.getItem('token')
  headers= new  HttpHeaders().set("Authorization","Token"+" "+this.token)
  
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
    this.token=sessionStorage.getItem('token')
    this.headers=this.headers.set("Authorization","Token"+" "+this.token)
    this.is_superuser = (sessionStorage.getItem('is_superuser') == 'true')
    if(this.token === null ){
      this.router.navigate(['login'])
      Emitters.authEmitter.emit(false);
      return false
    }
    Emitters.authEmitter.emit(true);
    Emitters.is_superuser.emit(this.is_superuser);
    return true
  }

  public home(){
    return this.http.get(Url.userviewUrl,{'headers': this.headers });
  }
  public role(usertype:boolean){
      this.is_superuser=usertype
  }

  public getrole(){
    return this.is_superuser;
  }
  
}
