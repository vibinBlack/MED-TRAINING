import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class LocalstorageService {

  temp:any
  constructor() { }

  checkSuperUser = () => {
     this.temp = sessionStorage.getItem("isSuperUser")
    //  console.log(this.temp)
     this.temp!=null ? this.temp = this.temp : this.temp = false
     console.log(this.temp)
     console.log(sessionStorage)
     return this.temp
  }

}
