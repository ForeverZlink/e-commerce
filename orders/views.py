from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from orders.models import ShoppingCart, Orders
from products.models import Product

# Create your views here.
def new_order(request,pk_product):
    
    product=Product.objects.get(pk=pk_product)
    user_pk  = request.user.pk
    
    user_instance = User.objects.get(pk=user_pk)
    order   = Orders.objects.create(
                user = user_instance , 
                product=product
            )
    order.save()
    return HttpResponseRedirect(reverse('products:home_page'))
    