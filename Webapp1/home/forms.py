from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from .models import Shopinfo
CustomUser = get_user_model()

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
            
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class SearchForm(forms.Form):
    
        keyword=forms.CharField(label='',max_length=50)
        
class Shop(forms.ModelForm):
    class Meta:
        model=Shopinfo
        fields='__all__'
        labels={'name':'店舗名','text':'詳細'}
    