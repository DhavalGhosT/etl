from django.shortcuts import render

def offer_view(request):
    return render(request, 'offers.html')

def main_view(request):
    return render(request, 'main.html')


