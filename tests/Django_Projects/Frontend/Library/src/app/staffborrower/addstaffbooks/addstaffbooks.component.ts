import { Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute,Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { BookService } from 'src/app/SharedServices/book.service';
import { StaffService } from 'src/app/SharedServices/staff.service';

@Component({
  selector: 'app-addstaffbooks',
  templateUrl: './addstaffbooks.component.html',
  styleUrls: ['./addstaffbooks.component.css']
})
export class AddstaffbooksComponent implements OnInit {

  constructor(private service : StaffService,private bookservice:BookService,private router : Router,private _Activatedroute:ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  @Input() info:any=[]
  borrowid:any
  status : boolean = false
  bookdata : any =[]
  formname !: string 
  
  id = new FormControl('');
  staff = new FormControl('');
  book=new FormControl('',[Validators.required]);
  issue_date=new FormControl('',[Validators.required,Validators.pattern('((?:19|20)[0-9][0-9])-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])')]);
  renewal_date=new FormControl('',[Validators.required,Validators.pattern('((?:19|20)[0-9][0-9])-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])')]);
  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.borrowid = params.get('id')
    })
    if(this.borrowid != 0){
      this.service.getstaffBorroweredit(this.borrowid).subscribe((res:any)=>{
          this.id.setValue(res.id),
          this.staff.setValue(res.staff),
          this.book.setValue(res.book),
          this.issue_date.setValue(res.issue_date),
          this.renewal_date.setValue(res.renewal_date)
      })
      this.status = false
      this.formname = "Staff Borrow Edit form"
    }
    else{
      this.staff.setValue(sessionStorage.getItem('staffid'))
      this.status = true
      this.formname = "Staff Borrow Add form"
      
    }
    this.bookservice.getBooks().subscribe(res=>{
      this.bookdata=res;
    })
  }
    
  borrowform = new FormGroup({
    id : this.id,
    staff : this.staff ,
    book:this.book,
    issue_date:this.issue_date,
    renewal_date:this.renewal_date,
  })

  updateBookinfo(){
    var staffid = sessionStorage.getItem('staffid');
    this.SpinnerService.show()
    this.service.putstaffBorrower(this.borrowform.value).subscribe(res=>{
      this.SpinnerService.hide(),
       this.router.navigate(["/staff-data/",staffid])},
       err=>{
         this.SpinnerService.hide();
       })
    
  }

  addBookinfo(){
    var staffid = sessionStorage.getItem('staffid');
    this.SpinnerService.show()
    this.service.poststaffBorrower(this.borrowform.value).subscribe(res=>{
      this.SpinnerService.hide(),
      this.router.navigate(["/staff-data/",staffid]) },
      err=>{
        this.SpinnerService.hide()
      }
      )
    
  }
}
