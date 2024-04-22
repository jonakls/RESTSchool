from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
