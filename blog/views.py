from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(" Blog -- DEV MART")

def home(request):
    return render(request,'blog/home.html')