from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.core.validators import MinValueValidator

# Create your models here.

class Type_of_Product(models.Model):
    type_product    = models.CharField(max_length= 100, primary_key=True)
    public_target   = models.CharField(max_length=100, unique=False,blank=False,null=False)

    def __str__(self) -> str:
        return self.type_product

class Mark_Product(models.Model):
    name_of_mark            = models.CharField(max_length= 100, primary_key=True)
    description_of_mark     = models.TextField()
    date_of_creation        = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_of_mark


class Imagem_Product(models.Model):
    name_image        = models.CharField(max_length=100,primary_key=True)
    imagem_of_product = models.ImageField(upload_to="media")

    def __str__(self) -> str:
        return self.name_image
    
class Product(models.Model):
    type_of_product = models.ForeignKey(Type_of_Product, on_delete=models.CASCADE)
    mark_of_product = models.ForeignKey(Mark_Product,on_delete=models.CASCADE)
    name            = models.CharField(max_length=100, primary_key=True)
    price           = models.DecimalField(max_digits=7,decimal_places=2)
    descripition    = models.TextField()
    inventory       = models.IntegerField(default=None,validators=[MinValueValidator(0)])
    imagem_product  = models.ManyToManyField(Imagem_Product)

    def __str__(self) -> str:
        return self.name

