from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from .views import product_information
from . import views 

app_name = 'product'  

urlpatterns = [
    path('', views.products, name='products'), #browse page
    path('new/', views.new_product, name='new_product'), # new_product is the name of the view function
    path('information/<int:pk>/', product_information, name='product_information'), 
    path('<int:id>/', views.product_detail, name='detail'),  # Detail view for the product
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]

