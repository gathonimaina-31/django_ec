# products/urls.py

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
<<<<<<< HEAD
    # Displays all products (view 2b)
    path('', views.list_products, name='list_products'), 
    
    # Allows adding a new product (view 2a)
    path('add/', views.add_product, name='add_product'), 
]
=======
    path('',views.home, name="home"),
    path('add_category/',views.add_category, name="add_category"),
    path('category_list/',views.category_list, name="category_list"),
]
>>>>>>> c946b71a4c3b62e9828adb53471db512e5008ef9
