from products.models import Category, Manufactorer
# from products.models import Category, Manufactorer, Cart, CartItem, userCartItem
# from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings


def category_menu_links(request):
    categoryLinks = Category.objects.all()
    return dict(clinks=categoryLinks)


def manufactorer_menu_links(request):
    manufactorerLinks = Manufactorer.objects.all()
    return dict(mlinks=manufactorerLinks)