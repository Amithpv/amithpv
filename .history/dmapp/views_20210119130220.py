from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fnDemo1(req):
    return render(req,'dm1.html')

def fnh(req):
    return HttpResponse("hellow")

def form(req)
    return render(req,'form.html')