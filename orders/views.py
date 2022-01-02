from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from orders.models import ShoppingCart, Orders,OrdersInCart
from products.models import Product


# Create your views here.

def finish_order_of_cart(request):
        #enviar  um email para o dono da loja com o pedido
    from django.core.mail import EmailMessage
    username_user = request.user.username
    pk_user=request.user.pk
    cart_of_user=ShoppingCart.objects.get(user__pk=pk_user)
    

    head_for_email=f'Novo pedido feito por {username_user}'
    content_for_email = ""
    for order_in_cart in cart_of_user.orders.all():
        order= Orders.objects.create(user=request.user, product=order_in_cart.product)
        text=f'Produto pedido:{order.product.name}  Preço:R${order.product.price}   Data e hora do pedido:{order.date_of_order}\n'
        content_for_email+=text
      
    
    email = EmailMessage(
            f'{head_for_email}',
            f"{content_for_email}",
            to=[request.user.email ],
            )
    email.send()
    #apaga todos os pedidos do carrinho de compras, pois o que é comprado não precisa estar no carrinho para as futuras compras 
    OrdersInCart.objects.all().delete()
    cart_of_user.orders.all().delete()

    return HttpResponseRedirect(reverse('products:home_page'))



def new_order_or_add_in_cart(request,pk_product,add_in_cart='false'):
    from django.core.mail import EmailMessage
    product=Product.objects.get(pk=pk_product)
    user_pk  = request.user.pk
    
    user_instance = User.objects.get(pk=user_pk)
    
    if add_in_cart =="true":
        order_for_cart = OrdersInCart.objects.create(user=request.user, product=product)
        order_for_cart.save()
        #parte provisória, irei mudar depois de criar o esquema de criação de usuário
        try:
        #testa se o usuário já possui um carrinho
            cart_of_user=ShoppingCart.objects.get(user__pk=user_pk)
        except:
            cart_of_user=ShoppingCart.objects.create(user=request.user)
        
        finally:
            cart_of_user=ShoppingCart.objects.get(user__pk=user_pk)

        cart_of_user.orders.add(order_for_cart)
    else:
        order   = Orders.objects.create(
                user = user_instance , 
                product=product
            )

        order.save()
        text=f'Produto pedido:{order.product.name}  Preço:R${order.product.price}   Data e hora do pedido:{order.date_of_order}\n'
        email = EmailMessage(
                f'Novo pedido de {request.user.username}',
                f"{text}",
                to=[request.user.email ],
                )
        email.send()
        
    return HttpResponseRedirect(reverse('products:home_page'))
    
def show_orders(request,orders_in_cart = 'false'):
    pk_user = request.user.pk
    if orders_in_cart == 'false':
        local = 'Pedidos já feitos'
        orders = Orders.objects.filter(user__pk=pk_user)
    else:
        local = 'Seu Carrinho de Compras'
        cart= ShoppingCart.objects.get(user__pk=pk_user)
        orders = cart.orders.all()
    print()
    return render(request, 'products/show_orders.html',
                context={'all_orders':orders,"local_of_orders_text":local
            })
