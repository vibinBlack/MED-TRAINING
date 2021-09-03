from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','is_staff','is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

    


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields= '__all__'
        #['title','author','ISBN','publication']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= '__all__'
        #['name','email','contact']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields= '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields='__all__'

class StaffBorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBorrower
        fields='__all__'

class StaffAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAccount
        fields='__all__'