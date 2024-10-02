from django.urls import path

from . import views

app_name = 'sell'  # line for namespacing

urlpatterns = [
    path('', views.index, name='index'),  # Redirect to the sell app's index view
    path('contact/', views.contact, name='contact'),  # Redirect to the sell app's contact view
]