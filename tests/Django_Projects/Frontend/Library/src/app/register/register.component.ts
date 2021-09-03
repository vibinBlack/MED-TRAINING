import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { AuthService } from '../SharedServices/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  hide =true;
  constructor(private authService : AuthService,private router:Router,private SpinnerService: NgxSpinnerService) { }

  ngOnInit(): void {
  }
  username = new FormControl('', [Validators.required]);
  email = new FormControl('',[Validators.required,Validators.pattern('(?![_.-])((?![_.-][_.-])[a-z\d_.-]){0,63}[a-z\d]@((?!-)((?!--)[a-z\d-]){0,63}[a-z\d]\.){1,2}([a-z]{2,14}\.)?[a-z]{2,14}')]);
  password = new FormControl('',[Validators.required,Validators.pattern('(?=.*[a-z])(?=.*[A-Z]).{6,}')]);
  staff = new FormControl(true);
  registerform = new FormGroup({
    username : this.username,
    email : this.email,
    password : this.password,
    staff : this.staff
  })
  onSubmit(): void {
    this.SpinnerService.show();
    this.authService.register(this.registerform.value).subscribe(data => {
      this.SpinnerService.hide();
      alert("Account created successfully!");
      this.router.navigate(["home"]);
    },
    err=>{
      this.SpinnerService.hide();
    }
    );
  }
  
}
