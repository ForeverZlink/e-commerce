from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render, reverse
import os
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
    token = os.environ.get('API_INSTAGRAM_TOKEN')
    url = f'https://graph.instagram.com/me/media?fields=media_url,caption,timestamp&access_token={token}'
    response=requests.get(url)
    data= json.loads(response.content) 
    media_content = data['data']

    return render(request,
            template_name="users/blog_admin.html",context={"all_media":media_content}
            )
