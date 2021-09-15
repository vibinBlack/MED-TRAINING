import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { SharedService } from '../shared.service';

@Component
({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit
{
  constructor(public service:SharedService,private router:Router) { }
  unauth:boolean=false;

  ngOnInit(): void {}

  Username= new FormControl('', [Validators.required]);
  Email= new FormControl('', [Validators.required, Validators.email]);
  Password= new FormControl('', [Validators.required]);
  registerForm = new FormGroup
  ({
    Username: this.Username,
    Email: this.Email,
    Password: this.Password
  });
  onSubmit():void
    {    
      let object=
      {
        "username": this.registerForm.get('Username')!.value,
        "email": this.registerForm.get('Email')!.value,
        "password": this.registerForm.get('Password')!.value
      }
      this.service.postRegister(object).subscribe(data=>
        {
          this.unauth=true;
          console.log(this.unauth)
        },
        (error:HttpErrorResponse)=>
        {
          this.unauth=false;
          console.log(this.unauth)
          alert("You are not authorized to Register");
          this.router.navigate(['home'])
        });
    }
}