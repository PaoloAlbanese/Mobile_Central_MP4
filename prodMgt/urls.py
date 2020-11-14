from django.urls import path
from . import views

#We're in prodMGT views.

urlpatterns = [
    path('add_product/', views.AddProduct, name='add_product'),
    path('add_brand/', views.AddBrand, name='add_brand'),
    path('add_side_pic/', views.AddSidePic, name='add_side_pic'),
    path('edit_product/', views.EditProduct, name='edit_product'),
    path('del_side_pic/', views.DelSidePic, name='del_side_pic'),

    
]