from django.urls import path
from . import views


urlpatterns = [
    path('all_products/', views.all_products, name='products'),
    path('Show_all_products/', views.showAll, name='show_all'),


]
