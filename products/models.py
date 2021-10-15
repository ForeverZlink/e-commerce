from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Type_of_Product(models.Model):
    type_product    = models.CharField(max_length= 100, unique=False,blank=False,null=False)
    public_target   = models.CharField(max_length=100, unique=False,blank=False,null=False)

    def __str__(self) -> str:
        return self.type_product

class Mark_Product(models.Model):
    name_of_mark            = models.CharField(max_length= 100, unique=False,blank=False,null=False)
    description_of_mark     = models.TextField()
    date_of_creation        = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_of_mark


class Imagem_Product(models.Model):
    name_image        = models.CharField(max_length=100,unique=True)
    imagem_of_product = models.ImageField()

    def __str__(self) -> str:
        return self.name_image
    
    
    
    

class Product(models.Model):
    type_of_product = models.ForeignKey(Type_of_Product, on_delete=models.CASCADE)
    mark_of_product = models.ForeignKey(Mark_Product,on_delete=models.CASCADE)
    name            = models.CharField(max_length=100, unique=True, blank=False,null=False)
    price           = models.FloatField()
    descripition    = models.TextField()
    imagem_product  = models.ManyToManyField(Imagem_Product)

    def __str__(self) -> str:
        return self.name
