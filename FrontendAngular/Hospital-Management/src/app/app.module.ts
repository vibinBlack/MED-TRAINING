import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './MyComponents/home/home.component';
import { LoginComponent } from './MyComponents/login/login.component';
import { FormsModule } from '@angular/forms';
import { DoctorsComponent } from './MyComponents/doctors/doctors.component';
import { CommonModule } from '@angular/common';
import { AdddoctorComponent } from './MyComponents/adddoctor/adddoctor.component';
import { UpdatedoctorComponent } from './MyComponents/updatedoctor/updatedoctor.component';
import { TimeslotComponent } from './MyComponents/timeslot/timeslot.component';
import { BookingComponent } from './MyComponents/booking/booking.component';
import { AddpatientComponent } from './MyComponents/addpatient/addpatient.component';
import { MyappointmentsComponent } from './MyComponents/myappointments/myappointments.component';
import { AllappointmentsComponent } from './MyComponents/allappointments/allappointments.component';
import { PatientsComponent } from './MyComponents/patients/patients.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    DoctorsComponent,
    AdddoctorComponent,
    UpdatedoctorComponent,
    TimeslotComponent,
    BookingComponent,
    AddpatientComponent,
    MyappointmentsComponent,
    AllappointmentsComponent,
    PatientsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    CommonModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
}) 
export class AppModule { }
