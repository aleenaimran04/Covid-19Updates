from django.db import models

# Create your models here.
class groupmembers(models.Model):
    std1=models.CharField(max_length=30)
    rollnost1=models.IntegerField()
    std2=models.CharField(max_length=30)
    rollnost2=models.IntegerField()
    std3=models.CharField(max_length=30)
    rollnost3=models.IntegerField()

class Complaintform(models.Model):
    firstname=models.CharField(max_length=45)
    lastname=models.CharField(max_length=45)
    email=models.EmailField()
    Country=models.CharField(max_length=45)
    complaint=models.CharField(max_length=500)

class registrationform(models.Model):
    firstname=models.CharField(max_length=45)
    lastname=models.CharField(max_length=45)
    email=models.EmailField()
    gender=models.CharField(max_length=20)
    cnic=models.CharField(max_length=20)
