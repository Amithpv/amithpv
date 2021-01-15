from django.shortcuts import render
from django.http import HttpRespoce


# Create your views here.
def fnDemo1(req):
    return render(req,'dm1.html')

def fnh(req):
    return HttpResponce("hellow")
