# from products.models import Category, Manufactorer
from products.models import Category, Manufactorer
from cart.models import Cart, CartItem, userCartItem
# from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def category_menu_links(request):
    categoryLinks = Category.objects.all()
    return dict(clinks=categoryLinks)


def manufactorer_menu_links(request):
    manufactorerLinks = Manufactorer.objects.all()
    return dict(mlinks=manufactorerLinks)

def counter(request):
    
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        if request.user.is_authenticated:
            try:
                cart_items=userCartItem.objects.filter(user=request.user)
                for cart_item in cart_items:
                    item_count += cart_item.quantity
            except ObjectDoesNotExist:
                item_count = 0
                
        else:
            try:
                cart= Cart.objects.filter(cart_id=_cart_id(request))
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
                for cart_item in cart_items:
                    item_count += cart_item.quantity
            except Cart.DoesNotExist:
                item_count = 0
            

    return dict(item_count=item_count)    