import { Injectable } from '@angular/core';
import {Observable, Subject} from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class CheckuserService {
  isAdmin: string = "no";
  updateAdmin =  new Subject<string>();
  temp:any;
  constructor() {
    // this.isAdmin = sessionStorage.getItem("isSuperUser")
    this.temp = sessionStorage.getItem("isSuperUser")
    this.temp != null ? this.isAdmin = this.temp : this.isAdmin ="no"
    this.updateAdmin.next(this.isAdmin);
  }


  setIsAdmin(data:string) {
    sessionStorage.setItem("isSuperUser", data);
    this.isAdmin = data;
    this.updateAdmin.next(this.isAdmin);
  }
    // this.isAdmin = Boolean(sessionStorage.getItem("isSuperUser"));
  }
