from django.db import models

# Create your models here.
class registration(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    cnic=models.CharField(max_length=30)

class complaint(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    city=models.CharField(max_length=30)
    desc=models.TextField()