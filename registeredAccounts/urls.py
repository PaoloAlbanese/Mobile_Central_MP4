from django.urls import path
from . import views

# We're in registeredAccounts urls.

urlpatterns = [
    path('account/create/', views.SignupView, name='signup'),
    path('account/signin/', views.SigninView, name='signin'),
    path('account/signout/', views.SignoutView, name='signout'),
    path('order_history/', views.orderHistory, name='order_history'),
    path('order/<int:order_id>/', views.viewOrder, name='order_detail'),
]
