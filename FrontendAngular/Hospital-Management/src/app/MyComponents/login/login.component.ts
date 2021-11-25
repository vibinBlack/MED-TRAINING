import { Component, Inject, OnInit } from '@angular/core';
import { LoginService } from 'src/app/Services/login.service';
import { Router } from '@angular/router';
import { AppComponent } from 'src/app/app.component';
import { LocalstorageService } from 'src/app/Services/localstorage.service';
import { CheckuserService} from 'src/app/Services/checkuser.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username:string="";
  password:string="";
  dict!:object;
  msg:string="";
  test!:object
  constructor(private api:LoginService,private router:Router,private api2:LocalstorageService, private userService: CheckuserService) {}

  ngOnInit(): void {
  }

  onSubmit() {
    this.dict = {'username':this.username, 'password':this.password}
    console.log(this.dict)
    this.api.CheckLogin(this.dict).subscribe(
      data=>{
        // localStorage.clear()
        console.log(data.token)
        // localStorage.setItem(this.username,JSON.stringify(data.token))
        // localStorage.setItem("0",JSON.stringify(this.username))
        sessionStorage.setItem("token",data.token)
        sessionStorage.setItem("username",this.username)
        console.log(sessionStorage)
        // this.checkRole()
        this.api.checkUserRole(this.dict).subscribe(
          data=>{ 
            // console.log(data.isSuperUser)
            console.log(data)
            if(data.isSuperUser===true)
              this.userService.setIsAdmin("yes")
            else
            this.userService.setIsAdmin("no")
            // sessionStorage.setItem("isSuperUser", String(data.isSuperUser))
            console.log(sessionStorage.getItem("isSuperUser"))
            this.router.navigate(["/"])
          },
          error => {
            console.log("ERROR "+error)
          }
        )
        // sessionStorage.setItem("isSuperUser",this.api2.checkSuperUser())
        
        console.log(localStorage)
        console.log(sessionStorage)
        // let obj = new AppComponent(this.router,this.api2)
        // obj.login()
      },
      error => {
        console.log("ERROR "+error)
        this.msg="Invalid Credentials"
      }
    )

    // this.router.navigate([""])
  }
  checkRole() {
    this.dict = {'username':this.username, 'password':this.password}
    console.log(this.dict)
    this.api.checkUserRole(this.dict).subscribe(
      data=>{ 
        // console.log(data.isSuperUser)
        console.log(data)
        sessionStorage.setItem("isSuperUser", String(data.isSuperUser))
        console.log(sessionStorage.getItem("isSuperUser"))
      },
      error => {
        console.log("ERROR "+error)
      }
    )
    // console.log(localStorage.getItem("isSuperUser"))
  }
}
