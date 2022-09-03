# from pickle import FALSE (NO SE NECESITA)
from django.shortcuts import render, HttpResponse
from django.template import loader 
# importamos el cargador (loader) y también HttpResponse para poder mostrar a los usuarios los datos de nuestra base de datos
from familiar.models import Familiar
# import datetime (NO SE NECESITA) Dejo estos comentarios para tener presente los errores


# Create your views here.
# Definimos nuestras vistas utilizando funciones

def catalogo(request):
    familiar_1 = Familiar(nombre = 'Claudia', biografia = 'Conyuge, psicopedagoga, le gustan las artesanías, nació en Dolores', edad = 59, cumpleanios = '1963-01-27')
    familiar_1.save() #con esto le indico a django que lo guarde en la base de datos
    
    familiar_2 = Familiar(nombre = 'Santiago', biografia = 'Hijo, Ingeniero, le gusta el tenis, disfruta los encuentros con amigos, nació en CABA', edad = 27, cumpleanios = '1995-02-06')
    familiar_2.save()
    
    familiar_3 = Familiar(nombre = 'Inés', biografia = 'Hija, estudia música en la EMPA, le gusta cantar y viajar, nacio en CABA', edad = 21, cumpleanios = '2000-07-18')
    familiar_3.save()
    
    plantilla = loader.get_template('familiares.html')
    
    familiares = {'familiares': [familiar_1, familiar_2, familiar_3]}
    
    documento = plantilla.render(familiares)
    
    return HttpResponse(documento)
