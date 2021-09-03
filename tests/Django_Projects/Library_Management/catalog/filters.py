import django_filters
from django import forms
from .models import *


class BookFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields='__all__'

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','isbn','publication']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model=Student
        fields='__all__'

class borrowerFilter(django_filters.FilterSet):
    class Meta:
        model=Borrower
        fields='__all__'


        