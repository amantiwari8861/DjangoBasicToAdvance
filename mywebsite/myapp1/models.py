from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255)
    mobileno=models.CharField(max_length=255)
