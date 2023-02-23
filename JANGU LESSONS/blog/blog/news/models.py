from django.db import models
import datetime
from django.contrib.auth.models import User
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



class Category(models.Model):
    cat_name=models.CharField(max_length=255)
    cover_img=models.ImageField(upload_to='category',blank=True,null=True)
    description=models.TextField()
    views = models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Kategoriya'
    def __str__(self):
        return self.cat_name

class UseProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=30)


    def __str__(self) ->str:
        return self.user

class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.CharField(max_length=100)
    post_view=models.IntegerField()
    created_add=models.DateTimeField(auto_now_add=True)
    created_add=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='yangilanish'


    def __str__(self):
        return self.title