from django.http import response
from django.test import TestCase
from products.models import *
from django.shortcuts import reverse
# Create your tests here.
class TestPagesWorks(TestCase):
    @classmethod
    def setUp(self):
        self.type_product     =Type_of_Product.objects.create(type_product="SmartPhone",public_target="Everybody")
        self.mark_product     =Mark_Product.objects.create(name_of_mark="Samsumg",
                description_of_mark="A mark of inovation")
       
     

    def test_if_home_page_works(self):
        url = '//'
        response = self.client.get(url)
        self.assertEqual(200,response.status_code)
    def test_detail_page_product_works(self):
        Product.objects.create(
            type_of_product=self.type_product,
            mark_of_product=self.mark_product,
            name='Galaxy A30',
            price="1000",
            descripition="A good cellphone",
            inventory=5,
            
        )
        url = reverse('products:detail_product',args=('Galaxy A30',))
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)
    

class TestViews(TestCase):
    @classmethod
    def setUp(self):
        self.type_product     =Type_of_Product.objects.create(type_product="SmartPhone",public_target="Everybody")
        self.mark_product     =Mark_Product.objects.create(name_of_mark="Samsumg",
                description_of_mark="A mark of inovation")
     

    def test_home_page_logic(self):
        Product.objects.create(
            type_of_product=self.type_product,
            mark_of_product=self.mark_product,
            name='Galaxy A30',
            price="1000",
            descripition="A good cellphone",
            inventory=5,
            
        )

    
        
    


        
