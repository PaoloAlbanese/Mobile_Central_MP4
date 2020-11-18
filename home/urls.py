from django.urls import path
from . import views

# We're in home views.

urlpatterns = [
    path('', views.latest, name='latest'),

]
