import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { StaffService } from '../SharedServices/staff.service';

@Component({
  selector: 'app-staffborrower',
  templateUrl: './staffborrower.component.html',
  styleUrls: ['./staffborrower.component.css']
})
export class StaffborrowerComponent implements OnInit {

  constructor(private service:StaffService,private router:Router,private _Activatedroute :ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  @Input() data:any=[]
  staff_id:any
  borrow_id:any
  booksinfo:any=[]
  staffinfo:any=[]
  toggle : boolean=false
  sts:any
  bookid:any
  title:any=[]
  search : any;

  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.staff_id = params.get('id')
    })
    sessionStorage.setItem('staffid',this.staff_id)
    // setTimeout(()=>{this.retrieveall()},2000)
    this.retrieveall();
    }
    retrieveall(){
      this.SpinnerService.show()
      this.service.getstaffBorrower(this.staff_id).subscribe(res=>{
        this.SpinnerService.hide()
        this.data=res;
    },
    err=>{
      this.SpinnerService.hide();
    })
    
    this.service.getStaffList(this.staff_id).subscribe(res=>{
      this.staffinfo=res;
    })
    }

  editstaffData(staff_book_info:any){
    this.router.navigate(['/editstaffstatus/',staff_book_info.id])
  }

  deletestaffData(staff_borrow:any){
    this.SpinnerService.show()
    this.service.deletestaffBorrower(staff_borrow.id).subscribe(res=>{
      this.SpinnerService.hide()
      this.retrieveall()},
      err=>{
        this.SpinnerService.hide();
      })
  }

  addStaffbooks(){
    this.router.navigate(['/editstaffstatus/','0'])
  }

  key : any 
  reverse : boolean =false
  sort(key:any){
    this.key = key ;
    this.reverse = !this.reverse;
  }
}
