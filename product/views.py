from django.shortcuts import render, get_object_or_404
from .models import Product  # Import the Product model

# Create your views here.
def information(request, pk):
    # Retrieve the product information from the database using the provided primary key.
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product/information.html',
     {'product': product})

    
    
