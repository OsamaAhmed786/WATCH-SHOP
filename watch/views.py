from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Startup(request):
    return render(request, 'start.html')
    

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def item(request):
    return render(request, 'shop-single.html')


