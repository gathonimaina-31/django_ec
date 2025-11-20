<<<<<<< HEAD
# products/views.py

from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Product

# 2a) View to insert (add) products
def add_product(request):
    # Dynamically create a form from the Product model fields
    ProductForm = modelform_factory(Product, fields=('name', 'category', 'price', 'description', 'image'))

    if request.method == 'POST':
        # request.FILES is required to handle the image upload
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('list_products') 
    else:
        form = ProductForm()

    context = {'form': form}
    # Renders the page from 'products/templates/products/add_product.html'
    return render(request, 'products/add_product.html', context)


# 2b) View to display all products
def list_products(request):
    # Retrieve all product records
    all_products = Product.objects.all().select_related('category')
    
    context = {
        'products': all_products,
    }
    # Renders the page from 'products/templates/products/product_list.html'
    return render(request, 'products/product_list.html', context)
=======
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def home(request):
    return render(request, "products/home.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # pass message
            return redirect("products:add_category")
    else:
        form = CategoryForm()
    return render(request,"products/category_form.html",{'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request,"products/category_list.html",{'categories':categories})
>>>>>>> c946b71a4c3b62e9828adb53471db512e5008ef9
