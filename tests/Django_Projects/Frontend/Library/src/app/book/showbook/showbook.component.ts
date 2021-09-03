import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { Emitters } from 'src/app/emitters/emitters';
import { BookService } from 'src/app/SharedServices/book.service';


@Component({
  selector: 'app-showbook',
  templateUrl: './showbook.component.html',
  styleUrls: ['./showbook.component.css']
})
export class ShowbookComponent implements OnInit {

  constructor(private bookList:BookService,private router:Router,private SpinnerService: NgxSpinnerService) { }

  Books:any=[];
  bk:any;
  search:any;

  ngOnInit(): void {
    // setTimeout(()=>{this.retrieveall()},2000)
    this.SpinnerService.show()
    this.retrieveall()
  }
  retrieveall(){
    this.bookList.getBooks().subscribe((books) => {
      this.Books=books;
      this.SpinnerService.hide()
    })
  }

  edit(id:any){
    this.router.navigate(['/edit/',id])
  }

  addClick(){
    this.router.navigate(["/edit",'0'])
  }


  delete(bk:any){
    this.SpinnerService.show()
    this.bookList.deleteBook(bk.isbn).subscribe(res=>{
      this.SpinnerService.hide(),
      this.retrieveall()},
      err=>{
        this.SpinnerService.hide();
      })
  }
  
  key : any = 'ISBN'
  reverse : boolean =false
  sort(key:any){
    this.key = key ;
    this.reverse = !this.reverse;
  }
}
