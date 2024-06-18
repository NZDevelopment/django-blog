from django.shortcuts import render
from django.http import HttpResponse #Nz

# Create your views here.
def my_blog(request):
    return HttpResponse("Hello, Blog!")
