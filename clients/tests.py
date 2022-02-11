from http import client
from django.test import TestCase
from django.shortcuts import render, reverse
from clients.views import login_custom
from django.contrib.auth.models import User
# Create your tests here.
class TestView(TestCase):
    def test_view_of_blog(self):
        import requests
        import json
        token = 'IGQVJXbDRMeWM5UnEza2hwLUpIN014dzJEcEphaUdBZAVdsbFBscC00emhLUFhJcld5bnMxTEJVc2ppVGdORjlqMVR4X2duYnF3UjRvQUJ5RlFKaExfY0oxQzQ4b3dVeHRKYlRvR1RCT25yblZAyelpybgZDZD'
        url = f'https://graph.instagram.com/me/media?fields=media_url,caption,timestamp&access_token={token}'

        response=requests.get(url)
        data= json.loads(response.content) 
        media_content = data['data']
        
        path = 'clients:blog_of_admin'
        response=self.client.get(reverse(path))
        self.assertEqual(response.status_code, 200)
        
    def test_login_custom(self):
        
        path = "clients:login_custom"
        email = 'carloscunha@gmail.com'
        username = "carlos"
        user_created=User.objects.create_user(username=username,password="123",email=email)
        user_created.save()
        response = self.client.post(reverse(path), data={'email':email,"password":"123"})
        self.assertEqual(response.status_code,302)
        
        
            
            
        
       
        