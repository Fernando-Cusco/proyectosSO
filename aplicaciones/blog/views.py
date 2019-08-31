import numpy as np
import pandas as pd
import json

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import ibm_cloud_sdk_core

from django.shortcuts import render
from .models import Post, Categoria, Libro
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


service = NaturalLanguageUnderstandingV1(version='2019-07-12',url='https://gateway.watsonplatform.net/natural-language-understanding/api', iam_apikey='JM1l-nZPsCwBdSfOLzP1b8lr4RREN6XDo_CiJ4a8HcNh')

# Create your views here.
def home(request):
    #<QueryDict: {'buscar': ['Que mas']}> buscar es el id
    querySet = request.GET.get("buscar")
    print(querySet)
    posts = Post.objects.filter(estado = True)
    if querySet:
        #Q busca lo que nos llega por GET si es igual titulo o en descripcion, distinct entra en caso ambos campos sean iguales
        posts = Post.objects.filter(Q(titulo__icontains =  querySet) | Q(descripcion__icontains = querySet)).distinct()
    #paginacion
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'post':posts})

def detallePost(request, slug):
    #post = Post.objects.get(slug = slug)
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'posts':post})

def generales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'General'))
    return render(request, 'generales.html', {'post': posts})

def programacion(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    return render(request, 'programacion.html', {'post': posts})

def tecnologia(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    print('Datos: ',posts)
    return render(request, 'tecnologia.html', {'post': posts})

def games(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos'))
    return render(request, 'videojuegos.html', {'post':posts})

def tutoriales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    return render(request, 'tutoriales.html', {'post':posts})

def libreria(request):
    querySet = request.GET.get("buscar")
    print('Buscando: ',querySet)
    car = []
    if querySet:
        datos = pd.read_csv('static/book_data1.csv', encoding = 'ISO-8859-1')
        descripcion = datos['book_title']
        titulo = []
        descri = []
        url = []
        pos = 0
        dfs = None
        for i in descripcion:
            try:
                dfs = service.analyze(html=i, features=Features(emotion=EmotionOptions(targets=[querySet]))).get_result()
                car.append(datos['book_title'][pos])
                car.append(datos['book_desc'][pos])
                car.append(datos['image_url'][pos])
                print(datos['book_title'][pos])
            except :
                print('No hay coincidencia')
                if dfs is None:
                    car.append(datos['book_title'][pos])
                    car.append(datos['book_desc'][pos])
                    car.append(datos['image_url'][pos])
                pos+=1
                #print(i, pos)

        print(car)
        descripciones = Libro.objects.filter(book_title = querySet)

    #car = "datos"
    return render(request, 'libreria.html', {'lib':car})
