import { Component,Inject,Input,OnInit  } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { LocalstorageService } from './Services/localstorage.service';
import { CheckuserService} from 'src/app/Services/checkuser.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [LocalstorageService]
})
export class AppComponent {

  title = 'Hospital-Management';
  isAdmin: string = "no";
  msg:string = ""
  // isSuperUser:boolean = false
  constructor(private router:Router,private api:LocalstorageService, private activatedRoute: ActivatedRoute, private checkuserService: CheckuserService){
    this.activatedRoute.params.subscribe( data => {
      this.isAdmin = this.checkuserService.isAdmin;
      this.checkuserService.updateAdmin.subscribe((value) => {
        this.isAdmin = value;
      })
      console.log(this.isAdmin);
    });
    // this.isAdmin = localStorage.getItem("isSuperUser")
    // this.isAdmin != null ? this.isAdmin = JSON.parse(this.isAdmin) : this.isAdmin=false
  }
  ngOnInit() {
  }
  logout() {
    sessionStorage.removeItem("username")
    sessionStorage.removeItem("token")
    this.checkuserService.setIsAdmin("no")
    // sessionStorage.setItem("isSuperUser","false")
    this.isAdmin = "no"
    // this.msg = "Logged Out Successfully"
    this.router.navigate(["/login"])
    // alert("Logged Out Successfully")
  }
  // login = () => {
  //   this.isAdmin = Boolean(this.api.checkSuperUser())
  //   console.log(this.isAdmin)
  //   console.log(localStorage)
  //   this.router.navigate(["/"])
  // }
}
