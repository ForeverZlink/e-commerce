from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from orders.models import ShoppingCart, Orders
from products.models import Product


# Create your views here.
def finish_order(request,pk_user):
        #enviar  um email para o dono da loja com o pedido
    from django.core.mail import EmailMessage
    username_user = request.user.username
    cart_of_user=ShoppingCart.objects.get(user__pk=pk_user)
    head_for_email=f'Novo pedido feito por {username_user}'
    content_for_email = ""
    for order in cart_of_user.orders.all():
        text=f'Produto pedido:{order.product.name}  Preço:R${order.product.price}   Data e hora do pedido:{order.date_of_order}\n'
        content_for_email+=text
      
    
    email = EmailMessage(
            f'{head_for_email}',
            f"{content_for_email}",
            to=[request.user.email ],
            )
    email.send()
    return HttpResponseRedirect(reverse('products:home_page'))



def new_order(request,pk_product):
    
    product=Product.objects.get(pk=pk_product)
    user_pk  = request.user.pk
    
    user_instance = User.objects.get(pk=user_pk)
    order   = Orders.objects.create(
                user = user_instance , 
                product=product
            )
    order.save()
    try:
        #testa se o usuário já possui um carrinho
        ShoppingCart.objects.get(user__pk=user_pk)
    except:
        ShoppingCart.objects.create(user=request.user)
        
    finally:
        cart_of_user=ShoppingCart.objects.get(user__pk=user_pk)
        cart_of_user.orders.add(order)
    

    


    return HttpResponseRedirect(reverse('products:home_page'))
    
def show_orders(request,pk_user):
    products = Orders.objects.filter(user__pk=pk_user)
    print(products)
    return HttpResponseRedirect(reverse('products:home_page'))
