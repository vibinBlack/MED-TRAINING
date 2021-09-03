import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
form ?: FormGroup;
  // username:any;
  // password : any;
  hide=true;
  message :any;
  error : boolean = false
  constructor(private http:HttpClient,private router:Router,private SpinnerService: NgxSpinnerService) { }
  
  ngOnInit(): void {
    // this.username="";
    // this.password = '';

  }
  
  username = new FormControl('', [Validators.required])
  password = new FormControl('',[Validators.required])
  loginform = new FormGroup({
    username : this.username,
    password : this.password
  })

  // getErrorMessage() {
  //   if (this.username.hasError('required')) {
  //     return 'You must enter a value';
  //   }

  //   return this.username.hasError('email') ? 'Not a valid email' : '';
  // }
  fb ?:FormBuilder
  onSubmit(){
    // let credentials={'username':this.username,'password':this.password}
    this.SpinnerService.show();
    this.http.post('http://127.0.0.1:8000/login',this.loginform.value).subscribe((res:any)=>{sessionStorage.setItem('token',res.token);
    this.SpinnerService.hide();
    this.router.navigate(["/home"])
    },
    err=>{
      this.error =true
      this.message="Please enter the correct credentials!";
      this.SpinnerService.hide();
      setTimeout(()=>{this.message=""},3000)
    }
  )
  }
}
