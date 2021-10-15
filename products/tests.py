from django.test import TestCase

# Create your tests here.
class TestPagesWorks(TestCase):
    def test_if_home_page_works(self):
        url = '//'
        response = self.client.get(url)
        self.assertEqual(200,response.status_code)