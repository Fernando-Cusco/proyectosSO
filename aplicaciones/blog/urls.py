from django.urls import path
from .views import home, programacion, tecnologia, generales, games, tutoriales, libreria, detallePost

urlpatterns = [
    path('', home, name = 'index'),
    path('programacion/', programacion, name = 'programacion'),
    path('tecnologia/', tecnologia, name = 'tecnologia'),
    path('generales/', generales, name = 'generales'),
    path('videojuegos/', games, name = 'videojuegos'),
    path('tutoriales/', tutoriales, name = 'tutoriales'),
    path('libreria/', libreria, name = 'libreria'),
    path('<slug:slug>', detallePost, name = 'detallePost'),
]
