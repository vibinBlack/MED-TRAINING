from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from catalog import views

'''
router = routers.DefaultRouter()
router.register(r'users', views.BookList)
router.register(r'student',views.StudentList)
router.register(r'borrower',views.BorrowerList)
'''

urlpatterns = [
    path('',views.index,name='home'),
    # path('login',views.loginUser, name='login'),
    # path('logout',views.logoutUser, name='logout'),
    path('add',views.add, name='add'),
    path('home',views.home,name='home'),
    path('search',views.search,name='search'),
    path('title',views.title,name='sort'),
    path('isbn',views.ISBN,name='sort'),
    path('author',views.author,name='sort'),
    path('delete/<int:id>',views.destroy,name='delete'),
    path('edit/<int:id>',views.edit,name='update'),
    path('update/<int:id>',views.update,name='update'),
    path('adduser',views.adduser,name="User Data"),
    path('borrowdata',views.borrowdata,name="Student books"),
    path('searchuser',views.searchuser,name="User Data"),
    path('deleteuser/<int:id>',views.deleteuser,name='delete'),
    path('edituser/<int:id>',views.edituser,name='update'),
    path('updateuser/<int:id>',views.updateuser,name='update'),
    path('namesort',views.namesort,name='Sorting'),


    url(r'^books/$',views.BookList.as_view()),
    url(r'^books/([0-9]+)$',views.BookDetails.as_view()),

    url(r'^students/$',views.StudentList.as_view()),
    url(r'^students/([0-9]+)$',views.StudentDetails.as_view()),

    url(r'^staff/$',views.StaffList.as_view()),
    url(r'^staff/([0-9]+)$',views.StaffDetails.as_view()),

    url(r'^students-data/$',views.StudentBorrowList.as_view()),
    url(r'^students-data/([0-9]+)$',views.StudentBorrowDetails.as_view()),
    url(r'^students-edit-data/([0-9]+)$',views.StudentBorrow.as_view()),

    url(r'^staff-data/$',views.StaffBorrowList.as_view()),
    url(r'^staff-data/([0-9]+)$',views.StaffBorrowDetails.as_view()),
    url(r'^staff-data-edit/([0-9]+)$',views.StaffBorrow.as_view()),

    path('registeruser',views.Register.as_view()),

    path('login',obtain_auth_token),
    path('userview',views.Userinfo.as_view()),
   
   
   
    path('logout',views.logoutApi),
    
    path('getter/<int:pk>',views.book_list,name="Listing"),
    path('update/<int:pk>',views.book_list,name="Update"),
    path('delete/<int:pk>',views.book_list,name="Delete"),
    path('bookcreate',views.book_list,name="Postdata")
    #path('', include(router.urls)),
    #path('snippets/', views.book_list),
   # path('book',views.BookList)
]

#urlpatterns = format_suffix_patterns(urlpatterns)