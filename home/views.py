from django.shortcuts import render
from products.models import Category, Manufactorer, Product, CaroPics
import re

# We're in home views.

# def latest(request):
#     """ A view to return the index page """

#     return render(request, 'home/index.html')


def latest(request):

    warnUser = request.session.get('warnUser')
    if not warnUser:
        warnUser = ""

    ids_in_user_cart = []
    olditems = ()

    cart_items = ()
    in_cart = []
    not_in_cart = []

    # if request.user.is_authenticated:
    #     if userCartItem:
    #         cart_items = userCartItem.objects.filter(user=request.user)

    #         for cart_item in cart_items:
    #             prod_id = cart_item.product.id
    #             prod = Product.objects.get(id=prod_id)
    #             if prod.stock > 0:
    #                 if cart_item.quantity > prod.stock:
    #                     cart_item.quantity = prod.stock
    #                     cart_item.save()

    #                     warnUser += "\n- the quantity for " + prod.name + \
    #                         " has decreased in your cart due to stock reduction - "
    #                     request.session['warnUser'] = warnUser

                        
    #             if prod.stock == 0:
    #                 cart_item.delete()

    #                 warnUser += "\n- " + prod.name + \
    #                     "- has run out of stock while it was still placed in the cart - "
    #                 request.session['warnUser'] = warnUser
                    

    #     try:

    #         if 'priortolog' in request.session:
    #             priortolog = request.session['priortolog']
    #             olditems = CartItem.objects.filter(cart=priortolog)

                
    #             for i in cart_items:
                    

    #             for cart_item in cart_items:
    #                 prod_id = cart_item.product.id
    #                 prod = Product.objects.get(id=prod_id)
    #                 cumulative_prod_qty = cart_item.quantity
    #                 for olditem in olditems:
    #                     if olditem.product.id == cart_item.product.id:
    #                         cumulative_prod_qty = cart_item.quantity + olditem.quantity
    #                         if prod.stock > 0:
    #                             if cumulative_prod_qty <= prod.stock:
    #                                 cart_item.quantity += olditem.quantity
    #                                 cart_item.save()
    #                             else:
    #                                 cart_item.quantity = prod.stock
    #                                 warnUser += "\n- the quantity for " + prod.name + \
    #                                     " has been adjusted in your cart due to changed stock availability - "
    #                                 request.session['warnUser'] = warnUser
    #                         if prod.stock == 0:
    #                             cart_item.delete()
    #                             warnUser += "\n- " + prod.name + \
    #                                 "- has run out of stock while it was being placed in the cart - "
    #                             request.session['warnUser'] = warnUser
                                
    #                 ids_in_user_cart.append(cart_item.product.id)

    #             for olditem in olditems:
    #                 if olditem.product.id not in ids_in_user_cart:
    #                     userCartItem.objects.create(
    #                         product=olditem.product, quantity=olditem.quantity, user=request.user)

                

    #             del request.session['priortolog']

    #     except ObjectDoesNotExist:
    #         print('non ha userCartese')

    # else:
    #     try:
    #         cart = Cart.objects.get(cart_id=_cart_id(request))
    #         cart_items = CartItem.objects.filter(cart=cart, active=True)

    #     except ObjectDoesNotExist:
    #         pass

    callheader = 'Check Out the Latest Arrivals!'
    products = Product.objects.filter(latest=True)
    new_arrivals_page = True
    pageTitle = 'Home'
    thisView = "latest"
    alphaArrow = "fa-sort-alpha-up"
    alphaVar = None
    alphaDir = "desc"
    AnnSort = ""
    euroL = None
    euroR = None
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
        'new_arrivals_page': new_arrivals_page,
        'pageTitle': pageTitle,
        'thisView': thisView,
        'alphaArrow': alphaArrow,
        'alphaDir': alphaDir,
        'euroSortL': euroSortL,
        'euroSortR': euroSortR,
        'euroDir': euroDir,
        'AnnSort': AnnSort,
        'cart_items': cart_items,
        'not_in_cart': not_in_cart,
        'warnUser': warnUser,
        'this_url': this_url,
        'referer_view': referer_view,
    }

    if cart_items and not request.user.is_authenticated:
        request.session['priortolog'] = cart.id

    return render(request, 'home/index.html', context)


def get_referer_view(request, default=None):
    ''' 
    Return the referer view of the current request

    Example:

        def some_view(request):
            ...
            referer_view = get_referer_view(request)
            return HttpResponseRedirect(referer_view, '/accounts/login/')
    '''

    # if the user typed the url directly in the browser's address bar
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return default

    # remove the protocol and split the url at the slashes
    referer = re.sub('^https?:\/\/', '', referer).split('/')

    # add the slash at the relative path's view and finished
    referer = u'/' + u'/'.join(referer[1:])
    return referer

