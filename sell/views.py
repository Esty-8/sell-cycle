from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import login
from product.models import Category, Product  # Import the Product model

from .forms import SignupForm # Import the Signup



def product_information(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/information.html', {
        'product': product
    })

# Create your views here.
def index(request):
    products = Product.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()  # Get all categories

    # Correct the return statement by passing the context as the third argument to render()
    return render(request, 'sell/index.html', {
        'categories': categories,  # Pass the categories to the template for display.
        'products': products,
    })

def contact(request):
    return render(request, 'sell/contact.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sell:login')  # Redirect to the sell app's index view after successful signup.
    else:
        form = SignupForm()

    return render(request, 'sell/signup.html' , {
        'form': form,  # Pass the form instance to the template for display.
    }) # The signup.html template will be rendered with the form instance.

