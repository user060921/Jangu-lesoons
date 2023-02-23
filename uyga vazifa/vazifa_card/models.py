from django.db import models
from django.contrib.auth.models import User


class sifat(models.Model):
    gender_type=(
        ('sifati','namunali'),('sifati','yaxshi'),('sifati','qoniqasiz')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    narxi = models.CharField(max_length=250)
    description = models.TextField(null=True)
    gender=models.CharField(max_length=255,choices=gender_type)
    def __str__(self):
        return f"{self.user} - {self.title}"


