from django.urls import path
from . import views

# We're in brand view.

urlpatterns = [
    path('brand/<int:num>/', views.brand, name='brand'),

]
