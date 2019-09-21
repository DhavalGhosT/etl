from django.shortcuts import render

# Create your views here.
def offer_view(request):
    return render(request, 'offer.html')