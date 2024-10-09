from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required 



# Create your views here.
from .models import Product  # Import the Product model
from .forms import ProductForm # Import the NewProduct

# Create your views here.
def information(request, pk):
    # Retrieve the product information from the database using the provided primary key.
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product/information.html', {
        'product': product
        # Pass the product object to the template for display
    })


@login_required  # Decorator to ensure that the user is logged in before accessing this view. 
def new_product(request):
    form = ProductForm()

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New Product',
    })
    
