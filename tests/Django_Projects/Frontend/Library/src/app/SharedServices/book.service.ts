import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {  Router } from '@angular/router';
import { Observable } from 'rxjs';
import {Url} from './urls';
 
@Injectable({
  providedIn: 'root'
})
export class BookService  {


  constructor(private http:HttpClient,private router:Router) { }

  is_superuser ?:boolean

  token=sessionStorage.getItem('token')
  headers= new  HttpHeaders().set("Authorization","Token"+" "+this.token)
  
  public getBooks(){
    return this.http.get(Url.booksUrl,{'headers': this.headers });
  }
  
  public getBookList(val:any){
    return this.http.get(Url.booksUrl+val,{'headers': this.headers });
  }

  public addBooks(val:any){
    return this.http.post(Url.booksUrl,val,{'headers': this.headers });
  }

  public editBook(val:any){
    console.log(val)
    return this.http.put(Url.booksUrl,val,{'headers': this.headers });
  }

  public deleteBook(val:any){
    return this.http.delete(Url.booksUrl+val,{'headers': this.headers });
  }
}
