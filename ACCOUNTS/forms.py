from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile,User,Contact

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user

class VendorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
        return user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
