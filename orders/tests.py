from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import login
from orders.models import Orders, OrdersInCart,ShoppingCart
from products.models import *
from django.shortcuts import reverse
# Create your tests here.
class TestViews(TestCase):
    @classmethod
    def setUp(self) :
        self.user             = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.user.save()
        self.type_product     =Type_of_Product.objects.create(type_product="SmartPhone",public_target="Everybody")
        self.mark_product     =Mark_Product.objects.create(name_of_mark="Samsumg",
                description_of_mark="A mark of inovation")
        self.product=Product.objects.create(
            type_of_product=self.type_product,
            mark_of_product=self.mark_product,
            name='Galaxy A30',
            price="1000",
            descripition="A good cellphone",
            inventory=5,
            
        )

        
        self.product.save()

        
    def test_remove_order_of_cart(self):
        self.client.login(username='john',password='johnpassword')
        path_remove_of_cart = 'orders:remove_of_cart'
        path_add_cart  = 'orders:new_order_or_add_in_cart'
        #na view, foi criado um novo pedido
        add_order_in_cart_response=self.client.get(reverse(path_add_cart,args=(self.product,"true"),))
        
        #Coloquei esse numero porque é o pk da OrderInCart que criei na linha anterior
        pk_do_pedido = 1

        delete_order_in_cart_response = self.client.get(reverse(path_remove_of_cart,args=(pk_do_pedido,),))
        self.assertEqual(add_order_in_cart_response.status_code,302)
        self.assertEqual(delete_order_in_cart_response.status_code,302)





    def test_create_new_order_or_add_in_cart(self):

        #testa a criação da order 
        self.client.login(username='john',password='johnpassword')
        path  = 'orders:new_order_or_add_in_cart'
        response=self.client.get(reverse(path,args=(self.product,)))
        self.assertEqual(response.status_code,302)
        order = Orders.objects.all()[0]
        
        self.assertEqual(order.product.name,"Galaxy A30")



        #parte do carrinho de compras
        self.shopping_cart = ShoppingCart.objects.create(user=self.user)
        self.shopping_cart.save()
        response =self.client.get(reverse(path,args=(self.product,"true"),))
        order_in_cart = OrdersInCart.objects.all()[0]
        self.assertEqual(response.status_code,302)
        self.shopping_cart.orders.add(order_in_cart)
        self.shopping_cart.orders.all().delete()
        print(self.shopping_cart.orders.all(),'fff')
        
    def test_show_orders(self):
        self.client.login(username='john',password='johnpassword')
        
        Orders.objects.create(user=self.user,product=self.product)
        path  = 'orders:show_orders'
        
        

        
        response=self.client.get(reverse(path))
        self.assertEqual(response.status_code,200)
        
    def test_finish_orders(self):
        self.client.login(username='john',password='johnpassword')
        
        order=OrdersInCart.objects.create(user=self.user,product=self.product)
        path  = 'orders:finish_order'
        

        self.shopping_cart=ShoppingCart.objects.create(user=self.user)
        self.shopping_cart.orders.add(order)
        response=self.client.get(reverse(path))
        