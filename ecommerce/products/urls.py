# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Displays all products (view 2b)
    path('', views.list_products, name='list_products'), 
    
    # Allows adding a new product (view 2a)
    path('add/', views.add_product, name='add_product'), 
]