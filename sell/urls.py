from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'sell'  # line for namespacing

urlpatterns = [
    path('', views.index, name='index'),  # Redirect to the sell app's index view
    path('contact/', views.contact, name='contact'),  # Redirect to the sell app's contact view
    path('login/', auth_views.LoginView.as_view(template_name='sell/login.html', authentication_form=LoginForm), name='login'),   # Redirect to the login
    path('signup/', views.signup, name='signup'),  # Redirect to the sell app's signup view
]