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
    path('LamborghiniHuracan', views.LamborghiniHuracan, name='LamborghiniHuracan'),
    path('Mersedesgel', views.Mersedesgel, name='Mersedesgel'),
    path('Nissan', views.Nissan, name='Nissan'),
    path('rollsroyce', views.rollsroyce, name='rollsroyce'),
    path('urus', views.urus, name='urus'),
    path('Rangerover', views.Rangerover, name='Rangerover'),
    path('Bentley', views.Bentley, name='Bentley'),
    path('Porscheone', views.Porscheone, name='Porscheone'),
    path('ferrari', views.ferrari, name='ferrari'),
    path('bmwx', views.bmwx, name='bmwx'),
    path('porschet', views.porschet, name='porschet'),
    path('mersedes', views.mersedes, name='mersedes'),
    path('rolsroyl', views.rolsroyl, name='rolsroyl'),
    path('audi', views.audi, name='audi'),
    path('cadillac', views.cadillac, name='cadillac'),
    path('bmwm', views.bmwm, name='bmwm'),
    path('mustang', views.mustang, name='mustang'),
    path('mclaren', views.mclaren, name='mclaren'),
    path('audir', views.audir, name='audir'),
    path('hyundai', views.hyundai, name='hyundai'),
    path('mersedesv', views.mersedesv, name='mersedesv'),

]

