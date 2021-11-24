from django.test import TestCase

from django.shortcuts import reverse
# Create your tests here.
class TestViews(TestCase):
    def test_create_new_order(self):
        self.client.get(reverse(''))