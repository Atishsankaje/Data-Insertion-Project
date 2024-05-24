from django.db import models


# Create your models here.
class Student(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
