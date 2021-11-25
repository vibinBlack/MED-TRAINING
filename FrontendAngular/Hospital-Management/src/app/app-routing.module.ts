import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { AdddoctorComponent } from './MyComponents/adddoctor/adddoctor.component';
import { AddpatientComponent } from './MyComponents/addpatient/addpatient.component';
import { AllappointmentsComponent } from './MyComponents/allappointments/allappointments.component';
import { BookingComponent } from './MyComponents/booking/booking.component';
import { DoctorsComponent } from './MyComponents/doctors/doctors.component';
import { HomeComponent } from './MyComponents/home/home.component';
import { LoginComponent } from './MyComponents/login/login.component';
import { MyappointmentsComponent } from './MyComponents/myappointments/myappointments.component';
import { PatientsComponent } from './MyComponents/patients/patients.component';
import { TimeslotComponent } from './MyComponents/timeslot/timeslot.component';
import { UpdatedoctorComponent } from './MyComponents/updatedoctor/updatedoctor.component';

export const routes: Routes = [
  {path:'', component: HomeComponent},
  {path:'login', component: LoginComponent},
  {path:'doctors', component: DoctorsComponent},
  {path:'adddoctor', component: AdddoctorComponent},
  {path:'updatedoctor/:docId', component: UpdatedoctorComponent},
  {path:'timeslot/:docId', component: TimeslotComponent},
  {path:'booking/:docId', component: BookingComponent},
  {path:'addpatient', component: AddpatientComponent},
  {path:'myappointments', component: MyappointmentsComponent},
  {path:'allappointments', component: AllappointmentsComponent},
  {path:'patients', component: PatientsComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
