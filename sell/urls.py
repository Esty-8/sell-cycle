from django.urls import path, include
from django.contrib.auth import views as auth_views


from .views import product_information, signup_view
from . import views
from .forms import LoginForm

app_name = 'sell'  


urlpatterns = [
    path('', views.index, name='index'),  # Redirect to the sell app's index view
    path('contact/', views.contact, name='contact'),  # Redirect to the sell app's contact view
    path('login/', auth_views.LoginView.as_view(template_name='sell/login.html', authentication_form=LoginForm), name='login'),   # Redirect to the login
    path('signup/', views.signup_view, name='signup'),  # Redirect to the sell app's signup
    path('information/<int:pk>/', product_information, name='product_information'),
  
    
]