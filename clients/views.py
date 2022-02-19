import email
from multiprocessing import context
from clients.models import Client
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
    if request.method =='POST':
        email_user = request.POST['email']
        password   = request.POST['password']
        try:
            user_searched=User.objects.get(email=email_user)
        except User.DoesNotExist:
            error= 'Por favor, digite um email válido'
            return render(request, template_name='users/login.html',context={'error_message':error})
        else:
            user_authenticate= authenticate(request=request,username=user_searched.username,password=password)
            if user_authenticate is not None:
                login(request,user_authenticate)
                return HttpResponseRedirect(reverse('products:home_page'))
            else:
                return HttpResponse('error')
    else:
        return render(request, template_name="users/login.html")
    
def create_user(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name   = request.POST['name']
        date_of_born = request.POST["date_of_born"]
        profision = request.POST['profision']
    

        user_object=User.objects.create_user(username=name,email=email,password=password)
        client_object=Client.objects.create(user=user_object,name=name,
                date_of_born=date_of_born,
                profision=profision
                )
    
    else:
        return render(request, template_name='users/new_user.html')