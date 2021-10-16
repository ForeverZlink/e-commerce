from django.shortcuts import render
from products.models import Product

# Create your views here.
def home_page(request):
    all_products = Product.objects.all()
    
    return render(request, 
                template_name='products/home_page.html',
                context={'products':all_products})