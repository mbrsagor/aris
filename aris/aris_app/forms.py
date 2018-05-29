from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, Select, RadioSelect, DateInput

class UserRegister(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'brd-rd5'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'brd-rd5'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'brd-rd5'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'brd-rd5'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
