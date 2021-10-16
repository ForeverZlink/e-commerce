from django.test import TestCase
from products.models import *
# Create your tests here.
class TestPagesWorks(TestCase):
    def test_if_home_page_works(self):
        url = '//'
        response = self.client.get(url)
        self.assertEqual(200,response.status_code)

class TestViews(TestCase):
    @classmethod
    def setUp(self):
        Type_of_Product.objects.create(type_product="SmartPhone",public_target="Everybody")


        

    def test_home_page_logic(self):
        print(Type_of_Product.objects.all())


        
