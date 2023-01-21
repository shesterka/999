from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('conditions', views.conditions, name='conditions'),
    path('rental', views.rental, name='rental'),
    path('contacts', views.contacts, name='contacts'),
    path('reviews', views.reviews, name='reviews'),
    path('premium', views.premium, name='premium'),
    path('sportcar', views.sportcar, name='sportcar'),
    path('vnedorozhnik', views.vnedorozhnik, name='vnedorozhnik'),
    path('minivan', views.minivan, name='minivan'),
]

