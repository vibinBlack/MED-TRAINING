from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from catalog.models import Book, Student,Borrower
from .serializers import *
from django.http import Http404



def userDBcall(userid):
    return User.objects.get(username=userid)


def get_book_by_id(isbn):
    try:
        return Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        raise Http404

def save_data(data):
    if data.is_valid():
        data.save()
        return Response(data.data,status=status.HTTP_201_CREATED)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

def get_books_data():
    try:
        books=Book.objects.all()
        return BookSerializer(books,many=True)
    except Book.DoesNotExist:
        raise Http404

def delete_book_by_id(pk):
    bookdata= get_book_by_id(pk)
    return bookdata.delete()

def get_student_by_id(studentid):
    try:
        return Student.objects.get(student_id=studentid)
    except Student.DoesNotExist:
        raise Http404

def saveBook(data):
    serializer = StaffSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer

def get_students_data():
    try:
        return Student.objects.all()
    except Student.DoesNotExist:
        raise Http404

def delete_student_by_id(pk):
    student_data = get_student_by_id(pk)
    return student_data.delete()
        
def studentBorrowDBcall(borrowid):
    return Borrower.objects.get(id=borrowid)

def studentBooks(sid):
    return Borrower.objects.filter(student=sid)

def studentdeleteBook(pk):
    studentborrow = studentBorrowDBcall(pk)
    return studentborrow.delete()

def staffDBcall(staffid):
    try :
        return Staff.objects.get(emp_id=staffid)
    except Staff.DoesNotExist :
        raise Http404

def staffALLdata():
    try:
        return Staff.objects.all()
    except Book.DoesNotExist:
        raise Http404

def staffdelete(pk):
    staff_data = staffDBcall(pk)
    return staff_data.delete()
    

def staffBorrowDBcall(borrowid):
    return StaffBorrower.objects.get(id=borrowid)

def staffBooks(sid):
    return StaffBorrower.objects.filter(staff=sid)

def staffdeleteBook(pk):
    staffborrow = staffBorrowDBcall(pk)
    return staffborrow.delete()

