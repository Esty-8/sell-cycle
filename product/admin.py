from django.contrib import admin
from .models import Category, Product  # Import the Category and Product models.

admin.site.register(Category)  # Register the Category model in the admin interface.
admin.site.register(Product)  # Register the Product model in the admin interface.


