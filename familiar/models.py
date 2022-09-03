from django.db import models

# Create your models here.
class Familiar(models.Model):
    # id: el campo id no es ncesario agragarlo porque lo van a tener tadas las instancias de manera automática, lo agrega django en nuestra base de datos
    nombre = models.CharField(max_length=30)
    biografia = models.TextField(max_length=300)
    convive = models.BooleanField(default= False)
    edad = models.IntegerField()
    cumpleanios = models.DateField()