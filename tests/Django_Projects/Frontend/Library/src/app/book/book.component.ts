import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../SharedServices/auth.service';
import { Emitters } from '../emitters/emitters';
import { HomeService } from '../SharedServices/home.service';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {
  message = ''
  role !: boolean;
  constructor(private http:HomeService,private service:AuthService) { }
   
  ngOnInit(): void {

    this.retrieveuser()
    // Emitters.is_superuser.emit((sessionStorage.getItem('is_superuser') == 'true'))
  }
  retrieveuser(){
    this.http.home().subscribe((res:any)=>{
      this.message = res.username;
      Emitters.authEmitter.emit(true);
      sessionStorage.setItem('is_superuser',res.is_superuser)
      this.role = (sessionStorage.getItem('is_superuser')=='true')
      Emitters.is_superuser.emit(this.role)
    }
    // err => {
    //   this.router.navigate(['login'])
    //   this.message = 'You are not logged in';
    //   Emitters.authEmitter.emit(false);
    // }
    )
  }
}
