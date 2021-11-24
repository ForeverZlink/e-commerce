from django.db.models.query import RawQuerySet
from django.shortcuts import render
from orders.models import ShoppingCart, Orders

# Create your views here.
def new_order(request,pk_product):
    user    = request.user
    order   = Orders.objects.create(
                user = user , 
                product=pk_product
            )
    order.save()
    