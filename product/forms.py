from django import forms

from .models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['featured_image','image', 'name', 'description', 'price', 'category']



class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['featured_image','image', 'name', 'description', 'price', 'is_sold']


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'form-control' to each field's widget
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'