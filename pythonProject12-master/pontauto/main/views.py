

from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def conditions(request):
    return render(request, 'main/conditions.html')

def rental(request):
    return render(request, 'main/rental.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def premium(request):
    return render(request, 'main/premium.html')

def sportcar(request):
    return render(request, 'main/sportcar.html')

def vnedorozhnik(request):
    return render(request, 'main/vnedorozhnik.html')

def minivan(request):
    return render(request, 'main/minivan.html')

def LamborghiniHuracan(request):
    return render(request, 'main/LamborghiniHuracan.html')

def Mersedesgel(request):
    return render(request, 'main/Mersedesgel.html')