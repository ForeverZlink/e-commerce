import email
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def adress_user(request, cep ):
    import json
    import requests
    url ="https://viacep.com.br/ws/25995287/json/"
    object = requests.get(url)
    print(json.loads(object.content))
    return HttpResponse(object)

  
def blog_of_admin(request):
    import requests
    import json
    token = 'IGQVJXbDRMeWM5UnEza2hwLUpIN014dzJEcEphaUdBZAVdsbFBscC00emhLUFhJcld5bnMxTEJVc2ppVGdORjlqMVR4X2duYnF3UjRvQUJ5RlFKaExfY0oxQzQ4b3dVeHRKYlRvR1RCT25yblZAyelpybgZDZD'
    url = f'https://graph.instagram.com/me/media?fields=media_url,caption,timestamp&access_token={token}'
    response=requests.get(url)
    data= json.loads(response.content) 
    media_content = data['data']

    return render(request,
            template_name="users/blog_admin.html",context={"all_media":media_content}
            )
def login_custom(request):

    email_user = request.POST['email']
    user_searched=User.objects.get(email=email_user)
    
    user_authenticate= authenticate(request=request,username=user_searched.username,password="123")
    login(request,user_authenticate)
    return HttpResponseRedirect(reverse('products:home_page'))
