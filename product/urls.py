from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from . import views 

app_name = 'product'  # line for namespacing

urlpatterns = [
    path('new/', views.new_product, name='new_product'), # new_product is the name of the view function
    path('<int:pk>/', views.information, name='product_information'), # product_information is the name of the view function
]

