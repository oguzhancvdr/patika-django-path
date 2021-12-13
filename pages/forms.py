from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
      'class': 'form-control text-secondary',
      'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
      'class': 'form-control text-secondary',
      'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
      'class': 'form-control text-secondary',
      'placeholder': 'Your email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
      'class': 'form-control text-secondary',
      'placeholder': 'Your phone number'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
      'class': 'form-control text-secondary',
      'rows': "6",
      'placeholder': 'Give us more details..'
    }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']