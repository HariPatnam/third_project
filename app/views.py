from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(request):
    return HttpResponse('<br> <h1> MY  INSATGRAM ID IS = "HARI_PATNAM_OFFICIAL" <h1><br>')
