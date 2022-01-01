from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey
from products.models import Product
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Orders(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_order= models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=200,default='')   
    delivered   = models.BooleanField(default=False)
    quantity    = models.IntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(7)])
    def __str__(self) -> str:
        return self.user.username


class OrdersInCart(models.Model):
    user     = models.ForeignKey(User,on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
class ShoppingCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    orders=models.ManyToManyField(OrdersInCart)
    def __str__(self) -> str:
        return  self.user.username
