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
        
    


        
