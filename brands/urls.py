from django.urls import path
from . import views

urlpatterns = [
    path('brand/<int:num>/', views.brand, name='brand'),
       
]