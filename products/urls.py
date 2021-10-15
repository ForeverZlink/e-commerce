from django.urls import path

from products.views import home_page

app_name="products"
urlpatterns = [
    path('',home_page,name='home_page')
]
