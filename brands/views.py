from django.shortcuts import render
from products.models import Manufactorer, Product
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

    # check if there is a warning to display to the user
    warnUser = request.session.get('warnUser')
    if not warnUser:
        warnUser = ""

    ids_in_user_cart = []
    olditems = ()

    cart_items = ()
    in_cart = []
    not_in_cart = []

    if request.user.is_authenticated:
        # check if the user had items in the cart since the last visit
        if userCartItem:
            cart_items = userCartItem.objects.filter(user=request.user)

            # check if items in the user's cart have
            # decreased or come to zero due to stock reduction.
            for cart_item in cart_items:
                prod_id = cart_item.product.id
                prod = Product.objects.get(id=prod_id)
                if prod.stock > 0:
                    if cart_item.quantity > prod.stock:
                        cart_item.quantity = prod.stock
                        cart_item.save()

                        # warn the user of any change
                        warnUser += "\n- the quantity for " + prod.name + \
                            " has decreased in your cart" +\
                            " due to stock reduction - "
                        request.session['warnUser'] = warnUser

                if prod.stock == 0:
                    cart_item.delete()
                    # warn the user the product(s) is sold out
                    warnUser += "\n- " + prod.name + \
                        "- has run out of stock while " +\
                        "it was still placed in the cart - "
                    request.session['warnUser'] = warnUser

        try:
            # check if the user added items in the cart before logging
            if 'priortolog' in request.session:
                priortolog = request.session['priortolog']
                olditems = CartItem.objects.filter(cart=priortolog)

                # add to pre-existing items in the cart since
                # the user's last visit, if any
                for cart_item in cart_items:
                    prod_id = cart_item.product.id
                    prod = Product.objects.get(id=prod_id)
                    cumulative_prod_qty = cart_item.quantity
                    for olditem in olditems:
                        if olditem.product.id == cart_item.product.id:
                            cumulative_prod_qty = cart_item.quantity +\
                                olditem.quantity
                            if prod.stock > 0:
                                # if a product was in the cart since the last
                                # visit of the user, and added again before
                                # logging back in, sum them up and see
                                # if the total is still in stock
                                if cumulative_prod_qty <= prod.stock:
                                    cart_item.quantity += olditem.quantity
                                    cart_item.save()
                                else:
                                    # if the product quantity added just before
                                    # logging in and the one already in the
                                    # cart since the last visit exceed stock,
                                    # warn the user
                                    cart_item.quantity = prod.stock
                                    warnUser += "\n- the quantity for "
                                    + prod.name + \
                                        " has been adjusted " + \
                                        "in your cart due " + \
                                        "to changed stock availability - "
                                    request.session['warnUser'] = warnUser
                            # warn the user if the product has ran out of stock
                            if prod.stock == 0:
                                cart_item.delete()
                                warnUser += "\n- " + prod.name + \
                                    "- has run out of stock while it " +\
                                    "was being placed in the cart - "
                                request.session['warnUser'] = warnUser

                    ids_in_user_cart.append(cart_item.product.id)

                # add the product to the user cart if not already existing
                for olditem in olditems:
                    if olditem.product.id not in ids_in_user_cart:
                        userCartItem.objects.create(
                            product=olditem.product,
                            quantity=olditem.quantity, user=request.user)

                # Only needed first thing after logging in
                del request.session['priortolog']

        except ObjectDoesNotExist:
            pass

    if request.user.is_authenticated:
        try:
            cart_items = userCartItem.objects.filter(user=request.user)
        except ObjectDoesNotExist:
            pass
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, active=True)
        except ObjectDoesNotExist:
            pass

    if request.user.is_authenticated:
        try:
            cart_items = userCartItem.objects.filter(user=request.user)
        except ObjectDoesNotExist:
            pass
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, active=True)
        except ObjectDoesNotExist:
            pass

    callheader = Manufactorer.objects.get(id=num)
    products = Product.objects.filter(manufactorer=num)
    pageTitle = Manufactorer.objects.get(id=num)
    thisView = "brand"
    AnnSort = ""
    alphaArrow = "fa-sort-alpha-up"
    alphaVar = None
    alphaDir = "desc"
    euroL = None
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
                alphaDir = "asc"
                AnnSort = " (Z to A)"
            else:
                alphaArrow = "fa-sort-alpha-up"
                alphaDir = "desc"
                AnnSort = " (A to Z)"

        if 'euroSortL' in request.GET:
            euroL = request.GET['euroSortL']
            if euroL == "fa-2x":
                euroSortL = ""
                euroSortR = "fa-2x"
                euroDir = "asc"
                AnnSort = "(Cheapest Last)"
            else:
                euroSortL = "fa-2x"
                euroSortR = ""
                euroDir = "desc"
                AnnSort = "(Cheapest First)"

    this_url = request.path
    referer_view = get_referer_view(request)

    context = {
        'products': products,
        'callheader': callheader,
        'pageTitle': pageTitle,
        'thisView': thisView,
        'num': num,
        'alphaArrow': alphaArrow,
        'alphaDir': alphaDir,
        'euroSortL': euroSortL,
        'euroSortR': euroSortR,
        'euroDir': euroDir,
        'AnnSort': AnnSort,
        'cart_items': cart_items,
        'not_in_cart': not_in_cart,
        'this_url': this_url,
        'referer_view': referer_view,
    }

    if cart_items and not request.user.is_authenticated:
        request.session['priortolog'] = cart.id

    return render(request, 'brands/brands.html', context)
