import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ApplyComponent } from './apply/apply.component';
import { ApproveComponent } from './approve/approve.component';
import { EmployeesComponent } from './employees/employees.component';
import { CrudComponent } from './employees/crud/crud.component';
import { UpdateComponent } from './employees/update/update.component';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { SharedService } from './shared.service';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  {path:'apply',component:ApplyComponent, canActivate:[SharedService]},
  {path:'approve',component:ApproveComponent, canActivate:[SharedService]},
  {path:'employees',component:EmployeesComponent, canActivate:[SharedService]},
  {path:'home',component:HomeComponent, canActivate:[SharedService]},
  {path:'profile',component:ProfileComponent, canActivate:[SharedService]},
  {path:'edit',component:CrudComponent, canActivate:[SharedService]},
  {path: 'update',component:UpdateComponent, canActivate:[SharedService]},
  {path: 'register',component:RegisterComponent, canActivate:[SharedService]},
  {path: '',component:LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
