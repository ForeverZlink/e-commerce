
from django.urls import path
from orders.views import new_order

urlpatterns = [
    path('new_order/<str:pk_product>/', new_order, name='new_order')
]
