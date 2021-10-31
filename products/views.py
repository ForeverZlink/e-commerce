from django.shortcuts import render
from products.models import Product,Imagem_Product

# Create your views here.
def home_page(request):
    all_products = Product.objects.all()
    
    


    return render(request, 
                template_name='products/home_page.html',
                context={'all_products':all_products})


def show_detail_product(request,pk): 
   
    product=Product.objects.get(pk=pk)
    return render(request,
                template_name='products/product_detail.html',
                context={'product':product}
                )