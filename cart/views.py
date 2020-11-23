from products.models import Product
from .models import Cart, CartItem, Order, OrderItem, userCartItem
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import stripe


# We're in cart views.


def cart(request):
    return render(request, 'cart/cart.html')


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        try:
            cart_item = userCartItem.objects.get(
                product=product, user=request.user)
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
                cart_item.save()

        except userCartItem.DoesNotExist:
            cart_item = userCartItem.objects.create(
                product=product, quantity=1, user=request.user)
            cart_item.save()

    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
            cart.save()
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product, quantity=1, cart=cart)
            cart_item.save()

    if 'source' in request.GET:

        return redirect(request.META.get('HTTP_REFERER'))
    else:

        return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):

    warnUser = request.session.get('warnUser')
    if not warnUser:
        warnUser = ""
    else:
        del request.session['warnUser'] # warning must appear only at first load of the page if needed.

    if request.user.is_authenticated:
        try:
            cart_items = userCartItem.objects.filter(user=request.user)
            for cart_item in cart_items:
                total += (cart_item.product.price*cart_item.quantity)
                counter += cart_item.quantity
        except ObjectDoesNotExist:
            print('fail in logged user cart details')
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, active=True)
            for cart_item in cart_items:
                total += (cart_item.product.price*cart_item.quantity)
                counter += cart_item.quantity
        except ObjectDoesNotExist:
            print('fail in anonymous user cart details')

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total*100)
    description = 'Mobile Central - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        print(request.POST)

        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddressLine1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingPostcode = request.POST['stripeBillingAddressZip']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddressLine1 = request.POST['stripeShippingAddressLine1']
            shippingCity = request.POST['stripeShippingAddressCity']
            shippingPostcode = request.POST['stripeShippingAddressZip']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']

            customer = stripe.Customer.create(email=email, source=token)
            charge = stripe.Charge.create(
                amount=stripe_total, currency='eur',
                description=description, customer=customer.id)

            # Create the Order

            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                    billingName=billingName,
                    billingAddressLine1=billingAddressLine1,
                    billingCity=billingCity,
                    billingPostcode=billingPostcode,
                    billingCountry=billingCountry,
                    shippingName=shippingName,
                    shippingAddressLine1=shippingAddressLine1,
                    shippingCity=shippingCity,
                    shippingPostcode=shippingPostcode,
                    shippingCountry=shippingCountry,


                )
                order_details.save()
                for order_item in cart_items:
                    or_item = OrderItem.objects.create(
                        product=order_item.product.name,
                        quantity=order_item.quantity,
                        price=order_item.product.price, order=order_details)
                    or_item.save()

                    # Reduce Stock
                    products = Product.objects.get(id=order_item.product.id)
                    products.stock = int(
                        order_item.product.stock - order_item.quantity)
                    products.save()
                    order_item.delete()

                    # print a message when the order is created
                    print('the order has been created')
                return redirect('thanks_page', order_details.id)
            except ObjectDoesNotExist:
                pass

        except stripe.error.CardError as e:
            return False, e
    this_url = request.path
    return render(request, 'cart/cart.html', dict(cart_items=cart_items,
                                                  total=total, counter=counter,
                                                  data_key=data_key,
                                                  stripe_total=stripe_total,
                                                  description=description,
                                                  warnUser=warnUser,
                                                  this_url=this_url))


def cart_remove(request, product_id):

    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart_item = userCartItem.objects.get(
            user=request.user, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    if 'source' in request.GET:
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('cart_detail')

    return redirect('cart_detail')


def cart_remove_product(request, product_id):

    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart_item = userCartItem.objects.get(
            user=request.user, product=product)
        cart_item.delete()
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.delete()

    return redirect('cart_detail')


def trashAll(request):
    if request.user.is_authenticated:
        cart_items = userCartItem.objects.filter(user=request.user)
        cart_items.delete()
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        cart_items.delete()
    return redirect('cart_detail')


def thanks_page(request, order_id):

    emailJSid = settings.EMAILJS_USER_ID
    emailJSsendOrd = settings.EMAILJS_SENDORD
    listone = ""

    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
        custName = customer_order.billingName
        captName = custName.title()
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        for item in order_items:
            sub_total = item.quantity * item.price
            item_name = str(item)
            item_qty = item.quantity
            item_price = item.price

            listone += "," + item_name + "," + \
                str(item_qty) + " X € " + str(item_price) + \
                ",subtotal: € " + str(sub_total)+","

    return render(request, 'cart/thankyou.html',
                  {'customer_order': customer_order, 'order': order,
                   'order_items': order_items, 'listone': listone,
                   'emailJSid': emailJSid,
                   'emailJSsendOrd': emailJSsendOrd, 'captName': captName})
