import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';

import { StudentService } from '../SharedServices/student.service';

@Component({
  selector: 'app-borrower',
  templateUrl: './borrower.component.html',
  styleUrls: ['./borrower.component.css']
})
export class BorrowerComponent implements OnInit {

  constructor(private service:StudentService , private router:Router,private _Activatedroute :ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  @Input() data:any=[]
  student_id:any
  booksinfo:any=[]
  studentinfo:any=[]
  toggle : boolean=false
  sts:any
  bookid:any
  title:any=[]
  search : any;

  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.student_id = params.get('id')
    })
    sessionStorage.setItem('studentid',this.student_id);
    // setTimeout(()=>{this.retrievedata()},2000)
    this.retrievedata()
  }
  retrievedata(){
    this.SpinnerService.show()
    this.service.getstudentBorrower(this.student_id).subscribe(res=>{
      this.SpinnerService.hide()
        this.data=res;
    },
    err=>{
      this.SpinnerService.hide();
    })
      
    this.service.getStudentList(this.student_id).subscribe(res=>{
      this.studentinfo=res;
    })
  }

  editData(student_data:any){
    this.router.navigate(['/editstudentstatus/',student_data.id])
  }

  deleteData(book:any){
    this.SpinnerService.show()
    this.service.deletestudentBorrower(book.id).subscribe(res=>{
      this.SpinnerService.hide(),
      this.retrievedata()
    },
    err=>{
      this.SpinnerService.hide();
    })
  }

  addUserinfo(){
    this.router.navigate(['/editstudentstatus/','0'])
  }


  key : any 
  reverse : boolean =false
  sort(key:any){
    this.key = key ;
    this.reverse = !this.reverse;
  }
}
