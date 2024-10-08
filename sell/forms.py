from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#  defined a new form 
class LoginForm(AuthenticationForm): 
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-70 py-4 px-5 rounded'
    }))
       
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-70 py-4 px-5 rounded'
    }))


class SignupForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # add 'first_name', 'last_name' fields if needed
        
        