from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fnDemo1(req):
    return render(req,'dm1.html')

def fnh(req):
    return HttpResponse("hellow")

def form(req):
    return render(req,'form.html')

def regform(req):
    return render(req,'regtable.html')    


def demoregform(req):
    return render(req,'hmereg.html')        

    def statimg(req):
    return render(req,'demoo.html')  