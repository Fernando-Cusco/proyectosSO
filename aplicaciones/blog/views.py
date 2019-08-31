import numpy as np
import pandas as pd
import json

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import ibm_cloud_sdk_core

from django.shortcuts import render
from .models import Libro
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


service = NaturalLanguageUnderstandingV1(version='2019-07-12',url='https://gateway.watsonplatform.net/natural-language-understanding/api', iam_apikey='JM1l-nZPsCwBdSfOLzP1b8lr4RREN6XDo_CiJ4a8HcNh')

# Create your views here.
def home(request):
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
