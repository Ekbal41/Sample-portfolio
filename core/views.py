from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):
    projects =Project.objects.order_by('-date')[1:4]
    projects1 =Project.objects.order_by('-date')[:1]
    ctx = {
        
        'projects1': projects1 ,
        'projects': projects ,
       
    }
    return render(request, 'index.html', ctx)

def test(request):
    return render(request, 'test.html')
