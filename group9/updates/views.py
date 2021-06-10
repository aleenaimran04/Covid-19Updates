from django.shortcuts import render
from updates.models import groupmembers
# Create your views here.
g=groupmembers(std1='Aleena Imran',rollnost1=183158,std2='Laiba Naveed',rollnost2=183209,std3='Minal Ejaz',rollnost3=183220)
g.save()