import email
from django.db import models
from django.http import request

# Create your models here.
class UserSign(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Password=models.CharField(max_length=40)

    def __str__(self):
        return self.Name