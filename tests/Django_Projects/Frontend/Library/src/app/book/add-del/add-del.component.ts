import { Component, OnInit,Input } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { Emitters } from 'src/app/emitters/emitters';
import { BookService } from 'src/app/SharedServices/book.service';


@Component({
  selector: 'app-add-del',
  templateUrl: './add-del.component.html',
  styleUrls: ['./add-del.component.css']
})
export class AddDelComponent implements OnInit {

  constructor(private service:BookService,private router:Router,private _Activatedroute :ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  id:any;
  book_data:any=[]
  status :boolean = false;
  formname !: string;

  isbn = new FormControl('', [Validators.required]);
  title = new FormControl('',[Validators.required]);
  author = new FormControl('',[Validators.required]);
  publication = new FormControl('',[Validators.required])

  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.id = params.get('id')
    })
    if(this.id != 0){
    this.service.getBookList(this.id).subscribe((res:any)=>{
    this.isbn.setValue(res.isbn),
    this.title.setValue(res.title),
    this.author.setValue(res.author),
    this.publication.setValue(res.publication)
    })
    this.status = false
    this.formname="Book Edit form";
  }
  else{
    this.status = true;
    this.formname="Book Add form";
  }
    // Emitters.status.subscribe((res)=>{
    // })
  }

  // this.service.getBookList(this.id).subscribe((res:any)=>{});
  

  bookform = new FormGroup({
    isbn : this.isbn,
    title : this.title,
    author : this.author,
    publication : this.publication
  })

  updateBook(){
    this.SpinnerService.show();
    this.service.editBook(this.bookform.value).subscribe(res=>{
      this.SpinnerService.hide();
      this.router.navigate(["books"])},
      err=>{
        this.SpinnerService.hide();
      }
      )
  }

  addBook(){
    this.SpinnerService.show();
    this.service.addBooks(this.bookform.value).subscribe(res=>{
      this.SpinnerService.hide();
      this.router.navigate(["books"]) },
      err=>{
        this.SpinnerService.hide();
      })
  }
  
}
