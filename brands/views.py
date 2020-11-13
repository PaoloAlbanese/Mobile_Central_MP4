from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Category, Manufactorer, Product, CaroPics
from home.views import get_referer_view
from django.core.exceptions import ObjectDoesNotExist
from cart.models import userCartItem, CartItem, Cart

# We're in brands views.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def brand(request, num):
    
    cart_items = ()
    in_cart=[]
    not_in_cart = []

    if request.user.is_authenticated:
        try:
            cart_items=userCartItem.objects.filter(user=request.user)
        except ObjectDoesNotExist:
            pass
    else:
        try:
            cart=Cart.objects.get(cart_id=_cart_id(request))
            cart_items=CartItem.objects.filter(cart=cart,active=True)
        except ObjectDoesNotExist:
            pass
    
    callheader = Manufactorer.objects.get(id=num)
    products = Product.objects.filter(manufactorer=num)
    pageTitle = Manufactorer.objects.get(id=num)
    thisView = "brand"
    AnnSort=""
    alphaArrow="fa-sort-alpha-up"
    alphaVar = None
    alphaDir ="desc"
    euroL=None
    euroR=None
    euroSortL = ""
    euroSortR = "fa-2x"
    euroDir = "asc"

    if cart_items:
        for i in cart_items:
            in_cart.append(i.product.id)
        

        for product in products:
            if product.id not in in_cart:
                not_in_cart.append(product.id)
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

            if sortkey == 'name':
                if direction == 'asc':
                   AnnSort = "(A to Z)" 
                elif direction == 'desc': 
                    AnnSort = " (Z to A)"
                elif alphaDir == 'asc':
                    AnnSort = "(A to Z)"
                elif alphaDir == 'desc':
                    AnnSort = " (Z to A)"

            elif sortkey == 'price':
                if direction == 'asc':
                    AnnSort = "(Cheapest First)"
                elif direction == 'desc':
                    AnnSort = "(Cheapest Last)"

        if 'alphaArrow' in request.GET:
            alphaVar = request.GET['alphaArrow']
            if alphaVar == "fa-sort-alpha-up":
                alphaArrow = "fa-sort-alpha-down"
                alphaDir ="asc"
                AnnSort = " (Z to A)"
            else:
                alphaArrow = "fa-sort-alpha-up"
                alphaDir ="desc"
                AnnSort = " (A to Z)"           

        if 'euroSortL' in request.GET:
            euroL= request.GET['euroSortL']
            if euroL == "fa-2x":
                euroSortL=""
                euroSortR="fa-2x"
                euroDir="asc"
                AnnSort = "(Cheapest Last)"
            else:
                euroSortL="fa-2x"
                euroSortR=""
                euroDir="desc"
                AnnSort = "(Cheapest First)"

    this_url = request.path
    referer_view = get_referer_view(request)

    context = {
        'products': products,
        'callheader': callheader,
        'pageTitle': pageTitle,
        'thisView' : thisView,
        'num':num,
        'alphaArrow':alphaArrow,
        'alphaDir':alphaDir,
        'euroSortL':euroSortL,
        'euroSortR':euroSortR,
        'euroDir':euroDir,
        'AnnSort':AnnSort,
        'cart_items':cart_items,
        'not_in_cart':not_in_cart,
        'this_url':this_url,
        'referer_view':referer_view,
    }


    return render(request, 'brands/brands.html', context)


