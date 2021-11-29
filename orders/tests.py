from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import login
from orders.models import Orders
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

    def test_create_new_order(self):
        self.client.login(username='john',password='johnpassword')
        path  = 'orders:new_order'
        response=self.client.get(reverse(path,args=(self.product,)))
        self.assertEqual(response.status_code,302)
        order = Orders.objects.all()[0]
        
        self.assertEqual(order.product.name,"Galaxy A30")
    def test_show_orders(self):
        self.client.login(username='john',password='johnpassword')
        
        Orders.objects.create(user=self.user,product=self.product)
        path  = 'orders:show_orders'
        
        user_pk=self.user.pk

        
        response=self.client.get(reverse(path,args=(user_pk,)))
        self.assertEqual(response.status_code,302)
        