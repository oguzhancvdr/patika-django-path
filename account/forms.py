from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# we already use User model in django so we did not use
# forms.ModelForm just like we did on ContactForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
      'class': 'form-control text-secondary',
      'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class': 'form-control text-secondary',
      'placeholder': 'Your password'
    }))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-secondary',
        'placeholder': 'Username'
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-secondary',
        'placeholder': 'First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-secondary',
        'placeholder': 'Last Name'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control text-secondary',
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-secondary',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control text-secondary',
        'placeholder': 'Re-Type Password'
    }))


    class Meta:
        model = User
        fields =['first_name','last_name', 'username', 'email', 'password1', 'password2',]