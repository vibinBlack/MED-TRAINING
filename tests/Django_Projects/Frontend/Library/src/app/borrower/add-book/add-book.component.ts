import { Component, Input, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute,Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { BookService } from 'src/app/SharedServices/book.service';
import { StudentService } from 'src/app/SharedServices/student.service';

@Component({
  selector: 'app-add-book',
  templateUrl: './add-book.component.html',
  styleUrls: ['./add-book.component.css']
})
export class AddBookComponent implements OnInit {

  constructor(private service : StudentService,private books:BookService,private router : Router,private _Activatedroute :ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  @Input() info:any=[]
  borrowid:any
  status : boolean = false
  bookdata : any =[]
  formname !: string;

    id = new FormControl('');
    student = new FormControl('');
    book=new FormControl('',[Validators.required]);
    issue_date=new FormControl('',[Validators.required,Validators.pattern('((?:19|20)[0-9][0-9])-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])')]);
    renewal_date=new FormControl('',[Validators.required,Validators.pattern('((?:19|20)[0-9][0-9])-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])')]);
  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.borrowid = params.get('id')
    })
    if(this.borrowid != 0){
      this.service.getstudentBorroweredit(this.borrowid).subscribe((res:any)=>{
          this.id.setValue(res.id),
          this.student.setValue(res.student),
          this.book.setValue(res.book),
          this.issue_date.setValue(res.issue_date),
          this.renewal_date.setValue(res.renewal_date)
      })
      this.formname = "Student Book Data Edit form";
      this.status = false
    }
    else{
      this.student.setValue(sessionStorage.getItem('studentid'))
      this.status = true
      this.formname = "Student Book Data Add form";
    }
    this.books.getBooks().subscribe(res=>{
      this.bookdata=res;
    })
  }

  borrowform = new FormGroup({
    id : this.id,
    student : this.student,
    book:this.book,
    issue_date:this.issue_date,
    renewal_date:this.renewal_date
  })
  updateBookinfo(){
    var studentid = sessionStorage.getItem('studentid') 
    this.SpinnerService.show()  
    this.service.putstudentBorrower(this.borrowform.value).subscribe(res=>{ 
      this.SpinnerService.hide()
      this.router.navigate(["/student-data/",studentid]) },
      err=>{
        this.SpinnerService.hide();
      })
   
  }

  addBookinfo(){
    var studentid = sessionStorage.getItem('studentid')  
    this.SpinnerService.show() 
    this.service.poststudentBorrower(this.borrowform.value).subscribe(res=>{
      this.SpinnerService.hide()
      this.router.navigate(["/student-data/",studentid]) },
      err=>{
        this.SpinnerService.hide();
      })
    
  }
}
