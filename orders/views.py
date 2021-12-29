from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from orders.models import ShoppingCart, Orders
from products.models import Product


# Create your views here.
def finish_order_of_cart(request,pk_user):
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



def new_order_or_add_in_cart(request,pk_product,add_in_cart='false'):
    from django.core.mail import EmailMessage
    product=Product.objects.get(pk=pk_product)
    user_pk  = request.user.pk
    
    user_instance = User.objects.get(pk=user_pk)
    order   = Orders.objects.create(
                user = user_instance , 
                product=product
            )

    order.save()
    if add_in_cart =="true":
        #parte provisória, irei mudar depois de criar o esquema de criação de usuário
        try:
        #testa se o usuário já possui um carrinho
            cart_of_user=ShoppingCart.objects.get(user__pk=user_pk)
        except:
            cart_of_user=ShoppingCart.objects.create(user=request.user)
        
        finally:
            cart_of_user=ShoppingCart.objects.get(user__pk=user_pk)

        cart_of_user.orders.add(order)
    else:
        text=f'Produto pedido:{order.product.name}  Preço:R${order.product.price}   Data e hora do pedido:{order.date_of_order}\n'
        email = EmailMessage(
                f'Novo pedido de {request.user.username}',
                f"{text}",
                to=[request.user.email ],
                )
        email.send()
        
    return HttpResponseRedirect(reverse('products:home_page'))
    
def show_orders(request,pk_user):
    products = Orders.objects.filter(user__pk=pk_user)
    print(products)
    return HttpResponseRedirect(reverse('products:home_page'))
