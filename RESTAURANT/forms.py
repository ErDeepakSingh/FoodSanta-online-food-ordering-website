from . import models as rest_models
from django import forms

class Restaurant_Form(forms.ModelForm):
    class Meta:
        model=rest_models.Add_Restaurant
        fields='__all__'

    rest_title = forms.CharField(max_length=150, label="Restaurant Name  ",widget=forms.TextInput({'class': 'form-control'}))
    locality = forms.CharField(max_length=150, label="Restaurant Locality ",
                                 widget=forms.TextInput({'class': 'form-control'}))
    city = forms.CharField(max_length=150, label="Restaurant City ",
                               widget=forms.TextInput({'class': 'form-control'}))
    pincode = forms.CharField(max_length=150, label="Restaurant Pincode ",
                           widget=forms.TextInput({'class': 'form-control'}))
    rest_image = forms.ImageField(label="Restaurant Image  ")
    rest_desc = forms.Textarea()

class Food_Details_Form(forms.ModelForm):
    class Meta:
        model=rest_models.FoodDetails
        fields='__all__'
    food_title = forms.CharField(max_length=150, label="Food Title  ",widget=forms.TextInput({'class': 'form-control'}))
    food_cuisine = forms.CharField(max_length=150, label="Food Cuisine  ",widget=forms.TextInput({'class': 'form-control'}))
    food_price = forms.CharField(max_length=150, label="Food Price  ",widget=forms.TextInput({'class': 'form-control'}))
    food_image = forms.ImageField(label="Food Image  ")
    food_Description = forms.TextInput()