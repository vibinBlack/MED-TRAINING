import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Employee } from 'src/app/employee';
import { SharedService } from 'src/app/shared.service';

@Component
({
  selector: 'app-crud',
  templateUrl: './crud.component.html',
  styleUrls: ['./crud.component.css']
})
export class CrudComponent implements OnInit 
{
  constructor(private fb: FormBuilder, private service:SharedService,private router:Router) { }

  ngOnInit(): void {}
  // createForm = this.fb.group({
  //   FirstName: [''],
  //   MiddleName: [''],
  //   LastName: [''],
  //   Gender: [''],
  //   BirthDate: [''],
  //   HireDate: [''],
  //   StreetAddress: [''],
  //   Address2: [''],
  //   City: [''],
  //   State: [''],
  //   PostalCode: [''],
  //   Country: [''],
  //   EmailAddress: [''],
  //   MobileNumber: ['']
  //}); 
  FirstName= new FormControl('', [Validators.required]);
  MiddleName= new FormControl('');
  LastName= new FormControl('', [Validators.required]);
  Gender= new FormControl('', [Validators.required]);
  BirthDate= new FormControl('', [Validators.required]);
  HireDate= new FormControl('', [Validators.required]);
  StreetAddress= new FormControl('', [Validators.required]);
  Address2= new FormControl('');
  City= new FormControl('', [Validators.required]);
  State= new FormControl('', [Validators.required]);
  PostalCode= new FormControl('', [Validators.required]);
  Country= new FormControl('', [Validators.required]);
  EmailAddress= new FormControl('', [Validators.required, Validators.email]);
  MobileNumber= new FormControl('', [Validators.required]);
  Designation= new FormControl('', [Validators.required]);
  Salary= new FormControl('', [Validators.required]);
  // , Validators.pattern('^[6-9]\d{9}$')
  createForm = new FormGroup({
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
    let object=
    {
      "First_Name": this.createForm.get('FirstName')!.value,
      "Middle_Name": this.createForm.get('MiddleName')!.value,
      "Last_Name": this.createForm.get('LastName')!.value,
      "Gender": this.createForm.get('Gender')!.value,
      "Birth_Date": this.createForm.get('BirthDate')!.value,
      "Hire_Date": this.createForm.get('HireDate')!.value,
      "Street_Address": this.createForm.get('StreetAddress')!.value,
      "Address2": this.createForm.get('Address2')!.value,
      "City": this.createForm.get('City')!.value,
      "State": this.createForm.get('State')!.value,
      "Postal_Code": this.createForm.get('PostalCode')!.value,
      "Country": this.createForm.get('Country')!.value,
      "Mobile_Number": this.createForm.get('MobileNumber')!.value,
      "Email_Address": this.createForm.get('EmailAddress')!.value,
      "Designation": this.createForm.get('Designation')!.value,
      "Salary": this.createForm.get('Salary')!.value
    }
    this.service.postEmp(object).subscribe(data=>
    {
      console.log(data);
      this.router.navigate(['register'])
    },
    (error)=>
    {
      alert("You are not authorized to view this page");
    });
  }
  back()
  {
    this.router.navigate(['employees'])
  }
}