import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { Emitters } from '../emitters/emitters';
import { AuthService } from '../SharedServices/auth.service';
import { HomeService } from '../SharedServices/home.service';
import { StudentService } from '../SharedServices/student.service';

@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.css']
})
export class StudentComponent implements OnInit {

  constructor(private service:StudentService,private router : Router,private home:HomeService,private auth :AuthService,private SpinnerService: NgxSpinnerService) { }

  Students :any=[];
  st:any;
  search :any;
  is_superuser : any;
  
  ngOnInit(): void {
    // setTimeout(()=>{this.retrieveall()},2000)
    this.retrieveall()
    this.is_superuser = (sessionStorage.getItem('is_superuser') == 'true')
  }

  displayColumns : string[] = ['student_id','name','email','contact','branch'];
  retrieveall(){
    this.service.getStudents().subscribe((stu) => {
      this.Students=stu;})
    // },
    // err=>{
    //   this.SpinnerService.hide();
    // })
  }

  editStudent(student_info:any){
    this.router.navigate(["/edit-students/",student_info.student_id])
  }

  addFunc(){
    this.router.navigate(["/edit-students/",'0'])
  }


  deleteStudent(id:any){
    this.SpinnerService.show()
    this.service.deleteStudent(id.student_id).subscribe(res=>{
      this.SpinnerService.hide();
      this.retrieveall()
    },
    err=>{
      this.SpinnerService.hide();
    })
  }

  studentData(info:any){
    this.router.navigate(["/student-data/",info.student_id])
  }

  key : any
  reverse : boolean =false
  sort(key:any){
    this.key = key ;
    this.reverse = !this.reverse;
  }
}
