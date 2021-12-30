
from django.urls import path
from orders.views import new_order_or_add_in_cart,show_orders,finish_order_of_cart


app_name='orders'
urlpatterns = [
    path('new_order_or_add_in_cart/<str:pk_product>/', new_order_or_add_in_cart, name='new_order_or_add_in_cart'),
    path('new_order_or_add_in_cart/<str:pk_product>/<str:add_in_cart>/', new_order_or_add_in_cart, name='new_order_or_add_in_cart'),
    path('show_orders/',show_orders,name="show_orders"),
    path('finish_orders/',finish_order_of_cart,name='finish_order')
]
