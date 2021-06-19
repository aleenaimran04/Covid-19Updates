from django.db.models.fields import PositiveIntegerField
from django.http import response
from django.shortcuts import render, HttpResponse
from .models import registration, complaint
from django.http.response import JsonResponse
from .serializer import registrationserializer,complaintserializer
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import io

from REGFORM import serializer

# Create your views here.

def home(request):
    return render(request, 'REGFORM/home.html')

def guidance(request):
    return render(request, 'REGFORM/guidance.html')

def pakistancases(request):
    return render(request, 'REGFORM/pakistancases.html')
    
def worldwidecases(request):
    return render(request, 'REGFORM/worldwidecases.html')

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

@csrf_exempt
def createapi(request):
    if request.method=="POST":
        stream=io.BytesIO(request.body)
        data=JSONParser().parse(stream)
        serializer=registrationserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'success':'data created'}
        return JsonResponse(msg,safe=False)


def CreateApi(request):
    if request.method=="POST":
        stream=io.BytesIO(request.body)
        data=JSONParser().parse(stream)
        serializer=complaintserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'success':'data created'}
        return JsonResponse(msg,safe=False)

    


        
    

            