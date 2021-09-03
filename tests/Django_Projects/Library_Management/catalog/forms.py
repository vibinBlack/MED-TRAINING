from django import forms
from django.db.models import fields
from .models import  *

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields="__all__"
