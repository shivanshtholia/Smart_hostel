from django.db import models


# class Signup(models.Model):
#     email=models.EmailField()
#     password=models.CharField(max_length=20)
    
class Hostel_user(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255,default=None)
    name=models.CharField(max_length=100,default=None)


class Admin(models.Model):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=100, default=None)
    last_name=models.CharField(max_length=100, default=None)
    password=models.CharField(max_length=300, default=None)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now_add=True)

