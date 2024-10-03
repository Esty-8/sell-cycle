from django.shortcuts import render
from product.models import Category, Product  # Import the Product model

from .forms import SignupForm # Import the Signup


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


def signup(request):
    form = SignupForm()

    return render(request, 'sell/signup.html' , {
        'form': form,  # Pass the form instance to the template for display.
    }) # The signup.html template will be rendered with the form instance.