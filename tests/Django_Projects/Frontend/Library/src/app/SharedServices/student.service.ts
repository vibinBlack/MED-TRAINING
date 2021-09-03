import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import {Url} from './urls';

@Injectable({
  providedIn: 'root'
})
export class StudentService {

  // url = "http://127.0.0.1:8000";
  constructor(private http:HttpClient,private router : Router) { }
  is_superuser ?:boolean

  token=sessionStorage.getItem('token')
  headers= new  HttpHeaders().set("Authorization","Token"+" "+this.token)
  

  public getStudents(){
    return this.http.get(Url.studentUrl,{'headers': this.headers });
  }

  public getStudentList(val:any){
    return this.http.get(Url.studentUrl+val,{'headers': this.headers });
  }

  public addStudents(val:any){
    return this.http.post(Url.studentUrl,val,{'headers': this.headers });
  }

  public editStudent(val:any){
    return this.http.put(Url.studentUrl,val,{'headers': this.headers });
  }

  public deleteStudent(val:any){
    return this.http.delete(Url.studentUrl+val,{'headers': this.headers });
  }



  public getstudentBorrower(val:any){
    return this.http.get(Url.studentdataUrl+val,{'headers': this.headers });
  }

  public getstudentBorroweredit(val:any){
    return this.http.get(Url.studentdataeditUrl+val,{'headers': this.headers });
  }

  public poststudentBorrower(val:any){
    return this.http.post(Url.studentdataUrl,val,{'headers': this.headers })
  }

  public putstudentBorrower(val:any){
    return this.http.put(Url.studentdataUrl,val,{'headers': this.headers })
  }

  public deletestudentBorrower(val:any){
    return this.http.delete(Url.studentdataUrl+val,{'headers': this.headers });
  }
}
