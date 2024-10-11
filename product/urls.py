from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



from . import views 

app_name = 'product'  # line for namespacing

urlpatterns = [
    path('new/', views.new_product, name='new_product'), # new_product is the name of the view function
    path('<int:pk>/', views.product_information, name='product_information'), # product_information is the name of the view function
    path('<int:id>/', views.product_detail, name='detail'),  # Detail view for the product
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]

