from django.db.models.fields import PositiveIntegerField
from django.http import response
from django.shortcuts import render, HttpResponse
from .models import registration, complaint


# Create your views here.

def home(request):
    return render(request, 'REGFORM/home.html')

def aboutcovid19(request):
    return render(request, 'REGFORM/aboutcovid19.html')

def symptoms(request):
    return render(request, 'REGFORM/symptom.html')
def precaution(request):
    return render(request, 'REGFORM/precaution.html')
def treatment(request):
    return render(request, 'REGFORM/treatment.html')
def vaccine(request):
    return render(request, 'REGFORM/vaccine.html')

def pakistancases(request):
    return render(request, 'REGFORM/pakistancases.html')


def registrationform(request):
    if request.method=="POST":
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        email= request.POST['email']
        phone= request.POST['phone']
        cnic= request.POST['cnic']
        ins=registration(firstname=firstname,lastname=lastname,email=email,phone=phone,cnic=cnic)
        ins.save()
        print("the data has been writen to db")


    return render(request, 'REGFORM/registrationform.html')

def complaintform(request):
    if request.method=="POST":
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        email= request.POST['email']
        phone= request.POST['phone']
        city=request.POST['city']
        desc=request.POST['desc']
        ins1=complaint(firstname=firstname,lastname=lastname,email=email,phone=phone,city=city,desc=desc)
        ins1.save()
    return render(request, 'REGFORM/complaintform.html')


    


        
    

            