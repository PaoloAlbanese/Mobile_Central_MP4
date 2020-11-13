from django.urls import path
from . import views

#We're in producto urls.

urlpatterns = [
    path('product_detail/<int:product_id>/', views.productPage, name='product_detail'),
       
]