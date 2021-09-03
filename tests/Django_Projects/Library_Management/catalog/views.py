from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate,login
from catalog.filters import *
from catalog.forms import *
import jwt,datetime
from django.contrib.auth.models import User


from catalog.models import Book, Student,Borrower

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *

from catalog.manager import *


# Create your views here.


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class BookList(APIView):
    def get(self,request):
        serializer = get_books_data()
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        response=save_data(serializer)
        return response
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        book = get_book_by_id(request.data['isbn'])
        serializer = BookSerializer(book,data=request.data)
        response=save_data(serializer)
        return response

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class BookDetails(APIView):
    def get(self,request,id):
        books=get_book_by_id(id)
        serializer = BookSerializer(books)
        return Response(serializer.data)
    
    def delete(self,request,id):
        operation=delete_book_by_id(id)
        if operation:
            return Response(data="Deleted successfully")
        return Response(data = "Not deleted")
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StudentList(APIView):
    def get(self,request):
        students = get_students_data()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        response=save_data(serializer)
        return response

    def put(self,request):
        student = get_student_by_id(request.data['student_id'])
        serializer = StudentSerializer(student,data=request.data)
        response=save_data(serializer)
        return response

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StudentDetails(APIView):
    def get(self,request,id):
        student=get_student_by_id(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def delete(self,request,id):
        operation=delete_student_by_id(id)
        if operation:
            return Response(data="Deleted successfully")
        return Response(data = "Not deleted")


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StaffList(APIView):
    def get(self,request):
        staffs = staffALLdata()
        serializer = StaffSerializer(staffs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StaffSerializer(data=request.data)
        response=save_data(serializer)
        return response

    def put(self,request):
        staff = staffDBcall(request.data['emp_id'])
        serializer = StaffSerializer(staff,data=request.data)
        response=save_data(serializer)
        return response

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StaffDetails(APIView):
    def get(self,request,id):
        staffs=staffDBcall(id)
        serializer = StaffSerializer(staffs)
        return Response(serializer.data)
    
    def delete(self,request,id):
        operation=staffdelete(id)
        if operation:
            return Response(data="Deleted successfully")
        return Response(data = "Not deleted")

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StudentBorrowList(APIView):
    
    def post(self,request):
        serializer = BorrowerSerializer(data=request.data)
        response=save_data(serializer)
        return response

    def put(self,request):
        book = studentBorrowDBcall(request.data['id'])
        serializer = BorrowerSerializer(book,data=request.data)
        response=save_data(serializer)
        return response

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StudentBorrowDetails(APIView):
    def get(self,request,id):
        books=studentBooks(id)
        serializer = BorrowerSerializer(books,many=True)
        return Response(serializer.data)
    
    def delete(self,request,id):
        operation=studentdeleteBook(id)
        if operation:
            return Response(data="Deleted successfully")
        return Response(data = "Not deleted")


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StudentBorrow(APIView):
    def get(self,request,id):
        data = studentBorrowDBcall(id)
        serializer = BorrowerSerializer(data,many=False)
        return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StaffBorrowList(APIView):
    
    def post(self,request):
        serializer = StaffBorrowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        book = staffBorrowDBcall(request.data['id'])
        serializer = StaffBorrowerSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StaffBorrowDetails(APIView):
    def get(self,request,id):
        books=staffBooks(id)
        serializer = StaffBorrowerSerializer(books,many=True)
        return Response(serializer.data)
    
    def delete(self,request,id):
        operation=staffdeleteBook(id)
        if operation:
            return Response(data="Deleted successfully")
        return Response(data = "Not deleted")
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StaffBorrow(APIView):
    def get(self,request,id):
        data = staffBorrowDBcall(id)
        serializer = StaffBorrowerSerializer(data,many=False)
        return Response(serializer.data)

class Register(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class Userinfo(APIView):
    def get(self,request):
        username = userDBcall(request.user)
        serializer=RegisterSerializer(username)
        return Response(serializer.data)




#Function Level Views

@api_view(['POST'])
def register_api(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mainpage(request):

    if request.method == "GET":
        username = userDBcall(request.user)
        serializer=RegisterSerializer(username)
        return Response(serializer.data)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_list(request,pk=0):

    if request.method == 'GET':
        books=get_book_by_id(pk)
        if(pk!=0):
            serializer = BookSerializer(books,many=False)
        else:
            serializer = BookSerializer(books,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        serializer = BookSerializer(data=book_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book = get_book_by_id(book_data['isbn'])
        serializer = BookSerializer(book,data=book_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        operation=delete_book_by_id(pk)
        data={}
        if operation:
            data['success'] = "Successful"
        else :
            data["failure"] = "Failure"
        return Response(data=data)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_list(request,pk=0):

    if request.method == 'GET':
        students=get_student_by_id(pk)
        
        if(pk!=0):
            serializer = StudentSerializer(students,many=False)
        else:
            serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        serializer = StudentSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = get_student_by_id(student_data['student_id'])
        serializer = StudentSerializer(student,data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation=delete_student_by_id(pk)
        data={}
        if operation:
            data['success'] = "Successful"
        else :
            data["failure"] = "Failure"
        return Response(data=data)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def staff_list(request,pk=0):

    if request.method == 'GET':
        staffs=staffDBcall(pk)
        if pk!=0:
            serializer = StaffSerializer(staffs,many=False)
        else:
            serializer = StaffSerializer(staffs,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        staff_data = JSONParser().parse(request)
        serializer = StaffSerializer(data=staff_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        staff_data = JSONParser().parse(request)
        staff = staffDBcall(staff_data['emp_id'])
        serializer = StaffSerializer(staff,data=staff_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation=staffdelete(pk)
        data={}
        if operation:
            data['success'] = "Successful"
        else :
            data["failure"] = "Failure"
        return Response(data=data)



@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_borrower(request,pk=0):

    if request.method == 'GET':
        data = studentBooks(pk)
        serializer = BorrowerSerializer(data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        serializer = BorrowerSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = studentBorrowDBcall(student_data['id'])
        serializer = BorrowerSerializer(student,data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation=studentdeleteBook(pk)
        data={}
        if operation:
            data['success'] = "Successful"
        else :
            data["failure"] = "Failure"
        return Response(data=data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_edit_borrower(request,pk=0):

    if request.method=='GET':
        data = studentBorrowDBcall(pk)
        serializer = BorrowerSerializer(data,many=False)
        return Response(serializer.data)
    

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def staff_borrower(request,pk=0):

    if request.method == 'GET':
        data = staffBooks(pk)
        serializer = StaffBorrowerSerializer(data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        staff_data = JSONParser().parse(request)
        serializer = StaffBorrowerSerializer(data=staff_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        staff_data = JSONParser().parse(request)
        staff = staffBorrowDBcall(staff_data['id'])
        serializer = StaffBorrowerSerializer(staff,data=staff_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation=staffdeleteBook(pk)
        data={}
        if operation:
            data['success'] = "Successful"
        else :
            data["failure"] = "Failure"
    return Response(data=data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def staff_edit_borrower(request,pk=0):
    if request.method=='GET':
        data = staffBorrowDBcall(pk)
        serializer = StaffBorrowerSerializer(data,many=False)
        return Response(serializer.data)

#MVT


@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        # print(password+" "+username)
        # user = authenticate(username=username, password=password)
        user = User.objects.filter(username = username).first()
        if user is None:
            raise AuthenticationFailed('User not Found')
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        token = Token.objects.create(user=username)
        print(token)
        response =Response()
        return response

@api_view(['GET']) 
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])       
def userView(request):
    if request.method == 'GET':
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.get(id=payload['id'])
        serializer = RegisterSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])        
def logoutApi(request):
    if request.method == 'POST':
        response = Response()
        # token = request.COOKIES.get('jwt')
        # response.delete_cookie('jwt')
        #
        id = request.data['userid']
        # print(id)
        # print(token)
        # payload = jwt.decode(token,'secret',algorithm=['HS256'])
        payload = { 'id': id,
                'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=1),
                'iat' : datetime.datetime.utcnow()
                }
        token =jwt.encode(payload , 'secret',algorithm = 'HS256').decode('utf=8')
        # time.sleep(32)
        print(token)
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True,samesite='None',secure=True,path='/')
        # print(response.set_cookie(key='jwt',value=token,samesite='None',secure=True,httponly=True))
        response.data={'jwt':token}
        return response


def refresh(request):
    pass

def index(request):
    return render(request,'home.html')
''' if request.user.is_anonymous:
        return redirect("/login")'''


def home(request):
    return render(request,'home.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def add(request):
    form=BookForm()
    if request.method == "POST":
        form=BookForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/search')
    return render(request,'add.html')

def destroy(request,id):
    Book.objects.get(ISBN=id).delete()    
    return redirect("/search") 

    
def edit(request, id):  
    book = Book.objects.get(ISBN=id)  
    return render(request,'edit.html', {'book':book}) 


def update(request,id):
    book = Book.objects.get(ISBN=id)  
    print(book)
    data = Bookform(request.POST, instance = book)
    print(data)  
    if data.is_valid():  
        data.save()  
        return redirect("/search")  
    return render(request, 'edit.html', {'book': book}) 

def search(request):
    books = Book.objects.all()
    myFilter=BookFilter(request.GET, queryset=books)
    books_data=myFilter.qs
    
    return render(request,'search.html',{'books':books_data,'myFilter':myFilter})

def title(request):
    Data_title = Book.objects.order_by('title')
    myFilter=BookFilter(request.GET , queryset=Data_title)
    books=myFilter.qs
    return render(request,'search.html',{'books':books,'myFilter':myFilter})

def ISBN(request):
    Data_isbn = Book.objects.order_by('ISBN')
    myFilter=BookFilter(request.GET , queryset=Data_isbn)
    books=myFilter.qs
    return render(request,'search.html',{'books':books,'myFilter':myFilter})

def author(request):
    Data_author = Book.objects.order_by('author')
    myFilter=BookFilter(request.GET , queryset=Data_author)
    books=myFilter.qs
    return render(request,'search.html',{'books':books,'myFilter':myFilter})

def calculateFine(request):
    pass

def adduser(request):
    form=StudentForm()
    if request.method == "POST":
        form=StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/searchuser')
    return render(request,'Users/adduser.html')

def borrowdata(request):
    books = Book.objects.all()
    students=Student.objects.all()
    if request.method == "POST":
        stu=request.POST.get('student')
        bok=request.POST.get('isbn')
        st=Student.objects.get(name=stu)
        bk=Book.objects.get(ISBN=bok)
        issuedate=request.POST.get("issuedate")
        renewdate=request.POST.get("renewdate")
        form=Borrower(student=st,book=bk,issue_date=issuedate,Renewal_date=renewdate)
        form.save()
        return redirect('/searchuser')
    return render(request,'Users/borrowdata.html',{'books':books,'students':students}) 


def searchuser(request):
    bookdata=Borrower.objects.all()
    bookFilter = borrowerFilter(request.GET,queryset=bookdata)
    books=bookFilter.qs
    return render(request,'Users/searchuser.html',{'books':books,"bookFilter":bookFilter})

def deleteuser(request,id):
    Borrower.objects.get(id=id).delete()    
    return redirect("/searchuser") 

def edituser(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'Users/edituser.html', {'book':student}) 


def updateuser(request,id):
    student = Student.objects.get(id=id)  
    data = StudentForm(request.POST, instance = student) 
    if data.is_valid():  
        data.save()  
        return redirect("/searchuser")  
    return render(request, 'Users/edituser.html', {'book': student}) 

def namesort(request):
    namesort = Borrower.objects.order_by('student')
    myFilter=borrowerFilter(request.GET , queryset=namesort)
    sort=myFilter.qs
    return render(request,'Users/searchuser.html',{'books':sort,'bookFilter':myFilter})







   