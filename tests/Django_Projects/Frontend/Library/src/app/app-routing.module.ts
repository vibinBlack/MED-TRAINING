import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StudentComponent } from './student/student.component';
import { AddEditComponent } from './student/add-edit/add-edit.component';
import { BookComponent } from './book/book.component';
import { ShowbookComponent } from './book/showbook/showbook.component';
import { componentFactoryName } from '@angular/compiler';
import { AddDelComponent } from './book/add-del/add-del.component';
import { StaffComponent } from './staff/staff.component';
import { EditstaffComponent } from './staff/editstaff/editstaff.component';
import { BorrowerComponent } from './borrower/borrower.component';
import { AddBookComponent } from './borrower/add-book/add-book.component';
import { AddstaffbooksComponent } from './staffborrower/addstaffbooks/addstaffbooks.component';
import { StaffborrowerComponent } from './staffborrower/staffborrower.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';

import { AuthService } from './SharedServices/auth.service';
import { HomeService } from './SharedServices/home.service';
import { LoginService } from './SharedServices/login.service';
import { ExitComponent } from './exit/exit.component';

const routes: Routes = [
  // {path : 'login/home',redirectTo:"/home",pathMatch:"full"},
  {path : '',redirectTo:"/login",pathMatch:"full"},
  { path : 'home',component:BookComponent,canActivate:[HomeService]},
  
  { path : 'books',component:ShowbookComponent,canActivate:[HomeService]},
  {path : 'edit',component:AddDelComponent,canActivate:[HomeService]},
  {path : 'edit/:id',component:AddDelComponent,canActivate:[HomeService]},
  {path : 'edit/books',redirectTo:"/books",pathMatch:"full"},
  {path : 'edit/:id/books',redirectTo:"/books",pathMatch:"full"},


  {path : 'students',component:StudentComponent,canActivate:[HomeService]},
  {path : 'edit-students/students',redirectTo:"/students",pathMatch:"full"},
  {path : 'edit-students/:id/students',redirectTo:"/students",pathMatch:"full"},
  {path : 'edit-students' , component:AddEditComponent,canActivate:[HomeService,AuthService]},
  {path : 'edit-students/:id' , component:AddEditComponent,canActivate:[HomeService,AuthService]},
  {path : 'student-data',component:BorrowerComponent,canActivate:[HomeService]},
  {path : 'student-data/:id',component:BorrowerComponent,canActivate:[HomeService]},
  {path : 'student-data/:id/students',redirectTo:"/students",pathMatch:"full"},
  {path : 'editstudentstatus/:id',component:AddBookComponent,canActivate:[HomeService]},
  {path : 'editstudentstatus/:id/student-data',redirectTo:"/students",pathMatch:"full"},
  {path : 'editstudentstatus/student-data',redirectTo:"/student-data",pathMatch:"full"},

  {path : 'staff' , component:StaffComponent,canActivate:[HomeService]},
  {path : 'edit-staff/staff',component:StaffComponent,canActivate:[HomeService,AuthService]},
  {path : 'edit-staff/:id/staff',component:StaffComponent,canActivate:[HomeService,AuthService]},
  {path : 'edit-staff', component:EditstaffComponent,canActivate:[HomeService,AuthService]},
  {path : 'edit-staff/:id', component:EditstaffComponent,canActivate:[HomeService,AuthService]},
  {path : 'staff-data',component:StaffborrowerComponent,canActivate:[HomeService]},
  {path : 'staff-data/:id',component:StaffborrowerComponent,canActivate:[HomeService]},
  {path : 'staff-data/:id/staff',redirectTo:"/staff",pathMatch:"full"},
  {path : 'editstaffstatus',component:AddstaffbooksComponent,canActivate:[HomeService]},
  {path : 'editstaffstatus/:id',component:AddstaffbooksComponent,canActivate:[HomeService]},
  {path : 'editstaffstatus/:id/staff-data',redirectTo:"/staff",pathMatch:"full"},
  {path : 'editstaffstatus/staff-data',redirectTo:"/staff-data",pathMatch:"full"},

  {path : 'register' ,component : RegisterComponent,canActivate:[HomeService,AuthService]},
  {path :'login' ,component :LoginComponent,canActivate:[LoginService]},

  {path:"**",component:ExitComponent},
  {path : '**/home',redirectTo:"/home",pathMatch:"full"}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
