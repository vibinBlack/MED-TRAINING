import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService implements CanActivate {
  token =sessionStorage.getItem('token')
  constructor(private router:Router) { }


  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
    this.token =sessionStorage.getItem('token')
    if(this.token != null ){
      this.router.navigate(['home'])
      return false
    }
    return true
  }
}
