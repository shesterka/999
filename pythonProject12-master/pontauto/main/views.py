

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

def Nissan(request):
    return render(request, 'main/Nissan.html')

def rollsroyce(request):
    return render(request, 'main/rollsroyce.html')

def urus(request):
    return render(request, 'main/urus.html')

def Rangerover(request):
    return render(request, 'main/Rangerover.html')

def Bentley(request):
    return render(request, 'main/Bentley.html')

def Porscheone(request):
    return render(request, 'main/Porscheone.html')

def bmwx(request):
    return render(request, 'main/bmwx.html')