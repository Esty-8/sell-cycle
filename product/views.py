from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product  # Import the Product model
from .forms import NewProductForm, EditProductForm  # Import the forms

# All products from the database that are not sold
def products(request):
    query = request.GET.get('query', '')  # Get the query parameter
    products = Product.objects.filter(is_sold=False)

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'product/products.html', {
        'products': products,
        'query': query,
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/detail.html', {
        'product': product
    })

def product_information(request, pk):
    # Retrieve the product information from the database using the provided primary key.
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product/information.html', {
        'product': product
    })

@login_required  # Ensures the user is logged in before accessing this view
def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)  # Handle file upload (images)

        if form.is_valid():
            product = form.save(commit=False)  # Create a product instance but don't save it to the database yet
            product.created_by = request.user  # Set the created_by field to the logged-in user
            product.save()  # Now save the product instance to the database
            return redirect('product:product_information', pk=product.id)  # Redirect to the product listed
            
    else:
        form = NewProductForm()  # If GET request, display an empty form

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New Product',
    })

@login_required
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)  # Handle file upload (images)

        if form.is_valid():
            form.save()
            return redirect('product:product_information', pk=product.id)  # Corrected to use pk
            
    else:
        form = EditProductForm(instance=product)  # If GET request, display the existing product form

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'Edit Product',
    })

@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    product.delete()

    return redirect('catalogue:index')  # Redirect to a relevant page after deletion
