from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model): # Define a Category model with fields for name
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Product(models.Model): # Define a Product model with fields for name, description, and category
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # links the Product model to the Category model using a foreign key
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True) # in case the product doesn't have a description
    price = models.FloatField() 
    image = models.ImageField(upload_to='products_images', blank=True, null=True) # to store the product image
    is_sold = models.BooleanField(default=False) # to track if the product has been sold
    created_at = models.DateTimeField(auto_now_add=True) # automatically set the created_at field to the current date and time when the product is created
    created_at = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE) # links the Product model to the Username model using a foreign key