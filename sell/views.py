from django.shortcuts import render
from product.models import Category, Product  # Import the Product model

# Create your views here.
def index(request):
    products = Product.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()  # Get all categories

    # Correct the return statement by passing the context as the third argument to render()
    return render(request, 'sell/index.html', {
        'categories': categories,  # Pass the categories to the template for display.
        'products': products,
    })

def contact(request):
    return render(request, 'sell/contact.html')
