from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,Permission
# Create your models here.
class myModel(models.Model):
    title=models.TextField()
    no=models.IntegerField()
    def __str__(self) -> str:
        return self.title
class Student(models.Model):
    email=models.EmailField(blank=False,unique=True)
    name=models.CharField(blank=False,max_length=100)
    rollno=models.CharField(blank=False,unique=True,primary_key=True,max_length=100)

    def __str__(self)->str:
        return self.name
    
