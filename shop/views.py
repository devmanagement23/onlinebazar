from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Index Shop")

def home(request):
    return render(request,'shop/home.html')

def about(request):
    return HttpResponse("shop - about link working")

def contact(request):
    return HttpResponse("shop - contact link working")

def tracker(request):
    return HttpResponse("shop - tracker link working")

def search(request):
    return HttpResponse("shop - search link working")

def productview(request):
    return HttpResponse("shop - productview link working")

def checkout(request):
    return HttpResponse("shop - checkout link working")
