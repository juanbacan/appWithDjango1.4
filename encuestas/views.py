# Create your views here.

from django.shortcuts import render

def encuestas(request):
    return render(request, 'encuestas/home.html')



    