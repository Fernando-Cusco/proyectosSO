from django.urls import path
from .views import libreria

urlpatterns = [
    path('libreria/', libreria, name = 'libreria'),
    path('libreria/', libreria, name = 'libreria'),
]
