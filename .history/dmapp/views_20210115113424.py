from django.shortcuts import render
from django.http import HttpRsponce


# Create your views here.
def fnDemo1(req):
    return render(req,'dm1.html')

def fnh(req):
    return HttpRsponce("hellow")
