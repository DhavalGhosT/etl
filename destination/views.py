from django.shortcuts import render

# Create your views here.
def destination(request):
    return render(request, 'destination.html')

def agra(request):
    return render(request,'Agra.html')

def dharamshala(request):
    return render(request,'Dharmashala.html')

def himachal(request):
    return render(request,'Himachal.html')

def rajasthan(request):
    return render(request,'Rajasthn.html')

def ladakh(request):
    return render(request,'Ladakh.html')