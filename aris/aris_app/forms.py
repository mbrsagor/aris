from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, Select, RadioSelect, DateInput
from .models import *



# User Register Forms
class UserRegister(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'brd-rd5'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'brd-rd5'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'brd-rd5'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'brd-rd5'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# Add new Item
class AddItem(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'price': TextInput(attrs={'class':'form-control'}),
            'discount_price': TextInput(attrs={'class':'form-control'}),
            'model': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
        }



# Blood Donor
class BloodDonor_Form(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = '__all__'
        widgets = {
            'bolood_type' : Select(attrs = {'class': 'form-control'}),
            'dononer_address' : Textarea(attrs = {'class': 'form-control'}),
        }



# About-Us Form
class AboutUs_Form(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'section_title': TextInput(attrs = {'class': 'brd-rd30'}),
            'section_desc': TextInput(attrs = {'class': 'brd-rd30'}),
            'aboutCompanyTitle': TextInput(attrs = {'class': 'brd-rd30'}),
        }




# Service Section form
class Service_Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'service_title': TextInput(attrs = {'class' : 'brd-rd30'}),
            'service_title': TextInput(attrs = {'class' : 'brd-rd30'}),
            'service_icon': TextInput(attrs = {'class' : 'brd-rd30'}),
            'tab_first_id': TextInput(attrs = {'class' : 'brd-rd30'}),
            'tab_second_id': TextInput(attrs = {'class' : 'brd-rd30'}),
        }




# Portfolio Section form
class Portfolio_Form(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        widgets = {
            'portfolio_title' : TextInput(attrs = {'class' : 'brd-rd30'}),
            'portfolio_class' : TextInput(attrs = {'class' : 'brd-rd30'}),
            'portfolio_data_filter' : TextInput(attrs = {'class' : 'brd-rd30'}),
        }




# Team Member section form
class TeamMember_Form(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'name' : TextInput(attrs = {'class' : 'brd-rd30'}),
            'designation' : TextInput(attrs = {'class' : 'brd-rd30'}),
        }
