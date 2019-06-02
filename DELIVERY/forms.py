
from django import forms
from . import models as delivery_models
class Delivery_Form(forms.ModelForm):
    class Meta:
        model=delivery_models.Delivery_address
        fields='__all__'

    firstname=forms.CharField(max_length=30,label='First Name ',widget=forms.TextInput({'class':'form-control'}))
    lastname=forms.CharField(max_length=30,label='Last Name ',widget=forms.TextInput({'class':'form-control'}))
    username=forms.CharField(max_length=30,label='User Name ',widget=forms.TextInput({'class':'form-control'}))
    email=forms.EmailField(max_length=50,label='Email ID ',widget=forms.TextInput({'class':'form-control'}))
    address1=forms.Textarea()
    address2=forms.Textarea()
    state = forms.CharField(max_length=30, widget=forms.TextInput({'class': 'form-control'}))
    district = forms.CharField(max_length=30, widget=forms.TextInput({'class': 'form-control'}))
    pincode = forms.CharField(max_length=30, widget=forms.TextInput({'class': 'form-control'}))
