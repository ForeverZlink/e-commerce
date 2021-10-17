from django.urls import path

from products.views import home_page
from django.conf import settings
from django.conf.urls.static import static



app_name="products"
urlpatterns = [
    path('',home_page,name='home_page')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
