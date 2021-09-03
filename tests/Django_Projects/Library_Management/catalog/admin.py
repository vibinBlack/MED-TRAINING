from django.contrib import admin
from catalog.models import *
# Register your models here.


admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)
admin.site.register(Staff)
admin.site.register(StaffBorrower)
admin.site.register(Account)
admin.site.register(StaffAccount)
