from django import forms

from .models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['featured_image','image', 'name', 'description', 'price', 'category']
