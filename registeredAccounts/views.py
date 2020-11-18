from django.conf import settings
from . forms import SignUpForm
from cart.models import Cart, CartItem, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# We're in registeredAccounts views.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def SignupView(request):
    emailJSid = settings.EMAILJS_USER_ID
    emailJSsignup = settings.EMAILJS_SIGNUP
    upform = ""
    dear = ""
    emailTo = ""
    yourID = ""
    dearCapt = ""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        upform = form

        if form.is_valid():
            form.save()

            dear = upform.cleaned_data.get('first_name')
            dearCapt = dear.capitalize()
            emailTo = upform.cleaned_data.get('email')
            yourID = upform.cleaned_data.get('username')
    else:
        form = SignUpForm()
    return render(request, 'registeredAccounts/signup.html', {'form': form,
                                                              'upform': upform,
                                                              'dear': dearCapt,
                                                              'emailTo':
                                                              emailTo,
                                                              'yourID':
                                                              yourID,
                                                              'emailJSid':
                                                              emailJSid,
                                                              'emailJSsignup':
                                                              emailJSsignup, })


def SigninView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    cart_items = CartItem.objects.filter(
                        cart=cart, active=True)

                except ObjectDoesNotExist:
                    pass

                return redirect('latest')
            else:
                return redirect('signup')

    else:
        form = AuthenticationForm()
    return render(request, 'registeredAccounts/signin.html', {'form': form})


def SignoutView(request):
    logout(request)
    return redirect('signin')


@login_required(redirect_field_name='next', login_url='signin')
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
    return render(request, 'registeredAccounts/orders_list.html',
                  {'order_details': order_details})


@login_required(redirect_field_name='next', login_url='signin')
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id=order_id, emailAddress=email)
        order_items = OrderItem.objects.filter(order=order)
    return render(request, 'registeredAccounts/order_detail.html',
                  {'order': order, 'order_items': order_items, })
