

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
