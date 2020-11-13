from django.shortcuts import render
from products.models import Product, CaroPics
from .models import Review


# We're in producto views.

def productPage(request, product_id):
    try:
        producto = Product.objects.get(id=product_id)
    except Exception as e:
        raise e

    if request.method == 'POST' and request.user.is_authenticated and request.POST['content'].strip()!='':
        Review.objects.create(product=producto, user=request.user, content = request.POST['content'])
    
    reviews = Review.objects.filter(product=producto,)
    caropics = CaroPics.objects.filter(product=producto)
    context = {
        'producto': producto,
        'reviews':reviews,
        'caropics':caropics,
        
    }
    
    return render(request, 'producto/product.html', context)