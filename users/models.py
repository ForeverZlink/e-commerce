from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Andress (models.Model):
    cep = models.CharField(max_length=20,blank=False,unique=False,null=False)
    state = models.CharField(max_length=50,blank=False,unique=False,null=False)
    city = models.CharField(max_length=150,blank=False,unique=False,null=False)
    district = models.CharField(max_length=150,blank=False,unique=False,null=False)
    complement = models.TextField()
    



class Client (models.Model):
    GENRES_CHOICES =[
        ('F','FEMININO'),
        ('M','MASCULINO'),
        ('O','OUTRO'),
    ]
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    date_of_born = models.DateField(null=False,blank=False,null=False)
    profision =  models.CharField(max_length=255, unique=False,blank=False)
    genre   = models.Choices(max_lenght =1, choices=GENRES_CHOICES)


