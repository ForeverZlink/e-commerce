from django.urls import path

from products.views import home_page, show_detail_product
from django.conf import settings
from django.conf.urls.static import static



app_name="products"
urlpatterns = [
    path('',home_page,name='home_page'),
    path('product_detail/<int:pk>/',show_detail_product, name='detail_product')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
