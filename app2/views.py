from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('heloo this is testing')