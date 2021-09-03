import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import {Url} from './urls'

@Injectable({
  providedIn: 'root'
})
export class StaffService {

  constructor(private http:HttpClient,private router:Router) { }

  is_superuser ?:boolean

  token=sessionStorage.getItem('token')
  headers= new  HttpHeaders().set("Authorization","Token"+" "+this.token)

  // STAFF API REQUESTS
  public getStaffs(){
    return this.http.get(Url.staffUrl,{'headers': this.headers });
  }

  public getStaffList(val:any){
    return this.http.get(Url.staffUrl+val,{'headers': this.headers });
  }

  public addStaffs(val:any){
    return this.http.post(Url.staffUrl,val,{'headers': this.headers });
  }

  public editStaff(val:any){
    return this.http.put(Url.staffUrl,val,{'headers': this.headers });
  }

  public deleteStaff(val:any){
    return this.http.delete(Url.staffUrl+val,{'headers': this.headers });
  }

  //Staff Books API

  public getstaffBorrower(val:any){
    return this.http.get(Url.staffdataUrl+val,{'headers': this.headers });
  }

  public getstaffBorroweredit(val:any){
    return this.http.get(Url.staffdataeditUrl+val,{'headers': this.headers });
  }

  public poststaffBorrower(val:any){
    return this.http.post(Url.staffdataUrl,val,{'headers': this.headers })
  }

  public putstaffBorrower(val:any){
    return this.http.put(Url.staffdataUrl,val,{'headers': this.headers })
  }

  public deletestaffBorrower(val:any){
    return this.http.delete(Url.staffdataUrl+val,{'headers': this.headers });
  }

}
