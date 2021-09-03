import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar'; 
import { MatIconModule } from '@angular/material/icon'; 
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input'; 
import { MatCardModule } from '@angular/material/card';
import {MatTableModule} from '@angular/material/table';
import {MatSortModule} from '@angular/material/sort';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { OrderModule } from 'ngx-order-pipe';
import { NgxSpinnerModule } from "ngx-spinner";

import 'hammerjs';

import { StudentComponent } from './student/student.component';
import { BookComponent } from './book/book.component';
import { ShowbookComponent } from './book/showbook/showbook.component';
import { AddDelComponent } from './book/add-del/add-del.component';
import { AddEditComponent } from './student/add-edit/add-edit.component';
import { StaffComponent } from './staff/staff.component';
import { EditstaffComponent } from './staff/editstaff/editstaff.component';
import { BorrowerComponent } from './borrower/borrower.component';
import { AccountComponent } from './account/account.component';
import { AddBookComponent } from './borrower/add-book/add-book.component';
import { StaffborrowerComponent } from './staffborrower/staffborrower.component';
import { AddstaffbooksComponent } from './staffborrower/addstaffbooks/addstaffbooks.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { NavComponent } from './nav/nav.component';



import { AuthService } from './SharedServices/auth.service';
import { HomeService } from './SharedServices/home.service';
import { StaffService } from './SharedServices/staff.service';
import { BookService } from './SharedServices/book.service';
import { ExitComponent } from './exit/exit.component';

@NgModule({
  declarations: [
    AppComponent,
    StudentComponent,
    BookComponent,
    ShowbookComponent,
    AddDelComponent,
    AddEditComponent,
    StaffComponent,
    EditstaffComponent,
    BorrowerComponent,
    AccountComponent,
    AddBookComponent,
    StaffborrowerComponent,
    AddstaffbooksComponent,
    RegisterComponent,
    LoginComponent,
    NavComponent,
    ExitComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatInputModule,
    MatTableModule,
    MatCardModule,
    MatSortModule,
    HttpClientModule,
    FlexLayoutModule,
    FormsModule,
    ReactiveFormsModule,
    Ng2SearchPipeModule,
    OrderModule,
    NgxSpinnerModule
  ],
  providers: [BookService,AuthService,HomeService,StaffService],
  bootstrap: [AppComponent]
})
export class AppModule { }
