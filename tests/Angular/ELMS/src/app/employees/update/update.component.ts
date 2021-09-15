import { Component, Input, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { SharedService } from 'src/app/shared.service';

@Component
({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent implements OnInit 
{
  Id? : number
  constructor(private service:SharedService,private router:Router) { }
  ngOnInit(): void 
  {    
    this.Id=history.state.Emp_No;
    this.FirstName.setValue(history.state.First_Name);
    this.MiddleName.setValue(history.state.Middle_Name);
    this.LastName.setValue(history.state.Last_Name);
    this.Gender.setValue(history.state.Gender);
    this.BirthDate.setValue(history.state.Birth_Date);
    this.HireDate.setValue(history.state.Hire_Date);
    this.StreetAddress.setValue(history.state.Street_Address);
    this.Address2.setValue(history.state.Address2);
    this.City.setValue(history.state.City);
    this.State.setValue(history.state.State);
    this.PostalCode.setValue(history.state.Postal_Code);
    this.Country.setValue(history.state.Country);
    this.EmailAddress.setValue(history.state.Email_Address);
    this.MobileNumber.setValue(history.state.Mobile_Number);
    this.Designation.setValue(history.state.Designation);
    this.Salary.setValue(history.state.Salary);
  }
  FirstName= new FormControl('',[ Validators.required,Validators.minLength(4)]);
  MiddleName= new FormControl('');
  LastName= new FormControl('');
  Gender= new FormControl('');
  BirthDate= new FormControl('');
  HireDate= new FormControl('');
  StreetAddress= new FormControl('');
  Address2= new FormControl('');
  City= new FormControl('');
  State= new FormControl('');
  PostalCode= new FormControl('');
  Country= new FormControl('');
  EmailAddress= new FormControl('');
  MobileNumber= new FormControl('');
  Designation= new FormControl('');
  Salary= new FormControl('');

  updateForm = new FormGroup({
    FirstName: this.FirstName,
    MiddleName: this.MiddleName,
    LastName: this.LastName,
    Gender: this.Gender,
    BirthDate: this.BirthDate,
    HireDate: this.HireDate,
    StreetAddress: this.StreetAddress,
    Address2: this.Address2,
    City: this.City,
    State: this.State,
    PostalCode: this.PostalCode,
    Country: this.Country,
    EmailAddress: this.EmailAddress,
    MobileNumber: this.MobileNumber,
    Designation: this.Designation,
    Salary: this.Salary,
  });

  onSubmit()
  {
    let object={
      "Emp_No":this.Id,
      "First_Name": this.updateForm.get('FirstName')!.value,
      "Middle_Name": this.updateForm.get('MiddleName')!.value,
      "Last_Name": this.updateForm.get('LastName')!.value,
      "Gender": this.updateForm.get('Gender')!.value,
      "Birth_Date": this.updateForm.get('BirthDate')!.value,
      "Hire_Date": this.updateForm.get('HireDate')!.value,
      "Street_Address": this.updateForm.get('StreetAddress')!.value,
      "Address2": this.updateForm.get('Address2')!.value,
      "City": this.updateForm.get('City')!.value,
      "State": this.updateForm.get('State')!.value,
      "Postal_Code": this.updateForm.get('PostalCode')!.value,
      "Country": this.updateForm.get('Country')!.value,
      "Mobile_Number": this.updateForm.get('MobileNumber')!.value,
      "Email_Address": this.updateForm.get('EmailAddress')!.value,
      "Designation": this.updateForm.get('Designation')!.value,
      "Salary": this.updateForm.get('Salary')!.value
    }
    console.log(object);
    this.service.putEmp(this.Id!,object).subscribe(data=>{console.log(data),this.router.navigate(['/employees'])},error=>console.error('Error!',error));
  }

  back()
  {
    this.router.navigate(['employees'])
  }
}