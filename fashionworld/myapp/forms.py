from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from myapp.models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','email','username','password1','password2')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('order_by','email','mobile','ship_address')
