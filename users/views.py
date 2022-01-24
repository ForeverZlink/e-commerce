from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse

# Create your views here.


def adress_user(request, cep ):
    import json
    import requests
    url ="https://viacep.com.br/ws/25995287/json/"
    object = requests.get(url)
    print(json.loads(object.content))
    return HttpResponse(object)

def instagram_api_admin(request):
    pass
    

def blog_of_admin(request):
    pass
