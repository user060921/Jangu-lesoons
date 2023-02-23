from django.db import models
import datetime
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    complated = models.BooleanField(default=False,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title}"


    
class Student(models.Model):
    gender_type=(
        ('M','Erkak'),('F','Ayol')
    )
    fullname=models.CharField(max_length=100, verbose_name='F.I.O')
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=16,unique=True)
    fee=models.FloatField(default=0)
    roll_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=50,choices=gender_type)
    addres=models.TextField()
    is_registered=models.BooleanField(default=False)
    birthDay=models.DateField(null=True,default=datetime.datetime.now())
    class Meta:
        verbose_name_plural='Talabalar'

    
    def __str__(self):
        return f'{self.fullname} | {self.roll_no}'


class ContactUs(models.Model):
    fullname=models.CharField(max_length=100, verbose_name='F.I.O')
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
