from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
    
class Employee(models.Model):
    GENDER=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    DESIGNATION=(
        ('Employee', 'Employee'),
        ('Manager', 'Manager'),
        ('HR', 'HR'),
    )

    Emp_No = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=14)
    Middle_Name = models.CharField(max_length=14,null=True)
    Last_Name = models.CharField(max_length=14)
    Birth_Date = models.DateField()
    Gender = models.CharField(max_length=6, choices=GENDER)
    Street_Address = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Postal_Code = models.PositiveIntegerField(default=0)
    Country = models.CharField(max_length=20)
    Mobile_Number = models.PositiveBigIntegerField(default=0)
    Email_Address = models.EmailField(max_length=70)
    Hire_Date = models.DateField()
    Designation = models.CharField(max_length=10, choices=DESIGNATION)
    Salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s %s %s' % (self.Emp_No, self.First_Name, self.Last_Name) 

class EmpLeaveRequest(models.Model):
    LEAVE_TYPE=(
        ('Personal', 'Personal'),
        ('Sick', 'Sick'),
    )
    LEAVE_STATUS=(
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Cancelled', 'Cancelled'),
    )

    EmpLeave_Req_ID = models.AutoField(primary_key=True)
    Emp_No = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="Emp_ID", default=0)
    Emp_FullName = models.CharField(max_length=50)
    Leave_Type = models.CharField(max_length=10, choices=LEAVE_TYPE)
    Begin_Date = models.DateField()
    End_Date = models.DateField()
    Requested_Days = models.PositiveIntegerField(default=0)
    Leave_Status = models.CharField(max_length=10, choices=LEAVE_STATUS, null=True, default='Pending')
    Emp_Comments = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '%s %s %s' % (self.EmpLeave_Req_ID, self.Emp_No, self.Emp_FullName)