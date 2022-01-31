from http import client
from django.test import TestCase
from django.shortcuts import render, reverse
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
        print(media_content)
        path = 'clients:blog_of_admin'
        response=self.client.get(reverse(path))
        self.assertEqual(response.status_code, 200)
        
        

        
            
            
        
       
        