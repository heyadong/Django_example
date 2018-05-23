from django.shortcuts import render
from django.shortcuts import reverse,redirect
from django.http import HttpResponse
# Create your views here.
def index(requset,name):
    return HttpResponse("your name is %s" %name)