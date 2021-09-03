import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Emitters } from '../emitters/emitters';
import { HomeService } from '../SharedServices/home.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  authenticated= false;
  id:number=0;
  is_superuser : boolean =false; 
  constructor(private http: HomeService,private router : Router) { }

  ngOnInit(): void {
    Emitters.authEmitter.subscribe(
      (auth: boolean) => {
        this.authenticated = auth;
      }
    );
    Emitters.is_superuser.subscribe(
      (auth: boolean) => {
        this.is_superuser = auth;
      }
    );
    Emitters.id.subscribe((id:number) => {
      this.id = id;
    });
  }


  logout(): void {
    sessionStorage.removeItem('token')
    sessionStorage.removeItem('is_superuser')
    sessionStorage.removeItem('staffid')
    sessionStorage.removeItem('studentid')
    this.authenticated=false
    this.router.navigate(['login'])  
  }

}
