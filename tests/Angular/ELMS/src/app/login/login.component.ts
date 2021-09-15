import { HttpClient, HttpResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators} from '@angular/forms';
import { Router } from '@angular/router';
import { SharedService } from '../shared.service';
import { JwtHelperService } from "@auth0/angular-jwt";

@Component
({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit 
{
  constructor(public service:SharedService,private router:Router, private http:HttpClient) { }
  credentials:boolean=false;
  helper = new JwtHelperService();
  hide = true;

  ngOnInit(): void
  {
    if(this.service.isUserLogedIn())
    {
      this.router.navigate(['home'])
    }
  }

  Username= new FormControl('', [Validators.required]);
  Password= new FormControl('', [Validators.required]);
  loginForm = new FormGroup
  ({
    Username: this.Username,
    Password: this.Password
  });

  onSubmit()
  {
    let object=
    {
      "username": this.loginForm.get('Username')!.value,
      "password": this.loginForm.get('Password')!.value
    }
    this.service.postLogin(object).subscribe((response:any) => 
    {
      this.credentials=false;
      if(response=="Invalid credentials")
      {
        this.credentials=true;
      }
      else
      {
        sessionStorage.setItem('jwt',response.token);
        // console.log(sessionStorage.getItem('jwt')); 
        // this.cookieService.set('jwt', response.jwt, { expires: 2, sameSite: 'Lax' });
        this.router.navigate(['home'])
        // .then(() => {window.location.reload();});
        // setTimeout(()=>{this.router.navigate(['/home']);},2000)
      }
    },
    (error)=>
    {
      this.credentials=true;
    });
  }
}