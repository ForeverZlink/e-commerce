
from django.urls import path
from orders.views import new_order,show_orders,finish_order


app_name='orders'
urlpatterns = [
    path('new_order/<str:pk_product>/', new_order, name='new_order'),
    path('show_orders/<int:pk_user>/',show_orders,name="show_orders"),
    path('finish_orders/<int:pk_user>/',finish_order,name='finish_order')
]
