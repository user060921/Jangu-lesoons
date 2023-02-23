from django.db import models
import datetime
class Student(models.Model):
    gender_type=(
        ('M','Erkak'),('F','Ayol')
    )
    fullname=models.CharField(max_length=100,verbose_name='F,I,O')
    email=models.EmailField(verbose_name='akkauntungizni kiriting')
    phone=models.CharField(max_length=13,unique=True,verbose_name='Telefon raqam')
    fee=models.FloatField(default=0)
    roll_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=50,choices=gender_type,verbose_name='ayol v erkak')
    addres=models.TextField(blank=True)
    is_regis=models.BooleanField(default=False)
    birthDay=models.DateField(null=True,
    default=datetime.datetime.now())


class ContactUs(models.Model):
    fullname=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subjects=models.CharField(max_length=250)
    text=models.TextField()
    created_add=models.DateTimeField(auto_now_add=True)
    updated_add=models.DateTimeField(auto_now=True)


class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.CharField(max_length=100)
    pst_view=models.IntegerField()
    created_add=models.DateTimeField(auto_now_add=True)
    updated_add=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural='Aloqalar'

    def __str__(self):
        return self.fullname


    class Meta:
        verbose_name_plural='Takliflar'

    def __str__(self):
        return f'{self.fullname}  {self.phone}'


