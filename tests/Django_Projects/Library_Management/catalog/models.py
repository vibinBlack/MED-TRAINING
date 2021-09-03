from enum import unique
from typing import Tuple
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin, User
from django.db.models.base import ModelState
from django.db.models.expressions import Value

# Create your models here.
# class MyAccountManager(BaseUserManager):
#     def create_user(self,email,username,password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have an usrername")
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,email,username,password):
#         user=self.create_user(
#             email=self.normalize_email(email),
#             password =password,
#             username = username
#         )
#         user.is_admin =True
#         user.is_staff=True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user




# class UsersAccount(AbstractBaseUser,PermissionsMixin):
#     email    = models.EmailField(verbose_name="email",max_length=60,unique=True)
#     username = models.CharField(max_length=30,unique=True)
#     date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
#     is_other= models.BooleanField(default=False)

#     USERNAME_FIELD='username'
#     # REQUIRED_FIELDS =['username']

#     objects =MyAccountManager()
    
#     def __str__(self) :
#         return self.username

#     def has_perm(self, perm, obj=None): 
#         return self.is_superuser

#     def has_module_perms(self, app_label): 
#         return self.is_superuser


class Book(models.Model):
    
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=200,primary_key=True)
    publication=models.CharField(max_length=200)


class Student(models.Model):

    student_id =models.CharField(max_length=20,primary_key=True,default='SOME STRING')
    name=models.CharField(max_length=200,default='SOME STRING')
    email=models.EmailField(max_length=100,default='SOME STRING')
    contact=models.CharField(max_length=10,default='SOME STRING')
    branch = models.CharField(max_length=50,default='SOME STRING')

class Staff(models.Model):

    emp_id = models.CharField(max_length = 20 ,primary_key=True,default = 'SOME STRING' )
    staff_name = models.CharField(max_length = 100 , default="SOME STRING")

class Borrower(models.Model):

    student=models.ForeignKey(Student,on_delete=models.CASCADE )
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date=models.DateField(null=True,blank=True)
    renewal_date=models.DateField(null=True,blank=True)

class StaffBorrower(models.Model):

    staff=models.ForeignKey(Staff,on_delete=models.CASCADE )
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date=models.DateField(null=True,blank=True)
    renewal_date=models.DateField(null=True,blank=True)




class Librarian(models.Model):

    staff_id = models.CharField(max_length=20,primary_key=True,default='Some string')
    name=models.CharField(max_length=200,default='SOME STRING')
   

class Account(models.Model):
    
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    no_borrowed_books=models.IntegerField(default=0)
    no_returned_books=models.IntegerField(default=0)
    no_lost_books=models.IntegerField(default=0)
    fine_amount=models.IntegerField(default=0)

class StaffAccount(models.Model):

    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    no_borrowed_books=models.IntegerField(default=0)
    no_returned_books=models.IntegerField(default=0)
    no_lost_books=models.IntegerField(default=0)
    fine_amount=models.IntegerField(default=0)

