import { Component, OnInit, Input } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { Emitters } from 'src/app/emitters/emitters';

import { StudentService } from 'src/app/SharedServices/student.service';

@Component({
  selector: 'app-add-edit',
  templateUrl: './add-edit.component.html',
  styleUrls: ['./add-edit.component.css']
})
export class AddEditComponent implements OnInit {

  constructor(private service:StudentService,private router:Router,private _Activatedroute :ActivatedRoute,private SpinnerService: NgxSpinnerService) { }

  id:any;
  student: any =[];
  status :boolean = false
  is_superuser =false
  formname !: string

  student_id =  new FormControl('',Validators.required);
  name = new FormControl('',Validators.required);
  email = new FormControl('',[Validators.required,Validators.pattern('(?![_.-])((?![_.-][_.-])[a-z\d_.-]){0,63}[a-z\d]@((?!-)((?!--)[a-z\d-]){0,63}[a-z\d]\.){1,2}([a-z]{2,14}\.)?[a-z]{2,14}')]);
  contact = new FormControl('',[Validators.required,Validators.pattern('([6-9]{1})([0-9]){9}')]);
  branch = new FormControl('',Validators.required);

  ngOnInit(): void {
    this._Activatedroute.paramMap.subscribe(params =>{
      this.id = params.get('id')
    })
    if (this.id !=0){
    this.service.getStudentList(this.id).subscribe((res:any)=>
    {
      this.student_id.setValue(res.student_id),
      this.name.setValue(res.name),
      this.email.setValue(res.email),
      this.contact.setValue(res.contact),
      this.branch.setValue(res.branch)
    })
    this.status = false
    this.formname = "Student Edit form"
  }
  else{
    this.status = true;
    this.formname = "Student Add form"
  }
  }
  
  studentform = new FormGroup({
    student_id : this.student_id,
    name :this.name,
    email :this.email,
    contact : this.contact,
    branch :this.branch
  })

  updateStudent(){
    this.SpinnerService.show()
    this.service.editStudent(this.studentform.value).subscribe(res=>{
      this.SpinnerService.hide();
      this.router.navigate(["students"])
     },
     err=>{
       this.SpinnerService.hide()
     })
  }

  addStudent(){
    this.SpinnerService.show();
    this.service.addStudents(this.studentform.value).subscribe(res=>{
      this.SpinnerService.hide();
      this.router.navigate(["students"]) },
    err=>{
      this.SpinnerService.hide();
    })
    
  }
}
