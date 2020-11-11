from django.urls import path
from . import views

# We're in Categories urls.

urlpatterns = [
    path('types/<int:num>/', views.types, name='types'),
       
]