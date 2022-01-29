import imp
from django.urls import path


from clients.views import blog_of_admin
app_name="clients"
urlpatterns = [
    path('blog/',blog_of_admin,name='blog_of_admin'),

]
