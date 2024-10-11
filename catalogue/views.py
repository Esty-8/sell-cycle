from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from product.models import Product


@login_required
def index(request):
    products = Product.objects.filter(created_by=request.user)

    return render(request, 'catalogue/index.html', {
        'products': products,
    })


