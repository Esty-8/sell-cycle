from django.urls import path
from . import views

app_name = 'product'  # line for namespacing

urlpatterns = [
    path('<int:pk>/', views.information, name='product_information'), # product_information is the name of the view function
]
