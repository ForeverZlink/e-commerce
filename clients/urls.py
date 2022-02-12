
from django.urls import path


from clients.views import blog_of_admin,login_custom
app_name="clients"
urlpatterns = [
    path('blog/',blog_of_admin,name='blog_of_admin'),
    path('login/',login_custom,name='login_custom')

]
