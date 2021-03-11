from django import forms
from .models import Truck_card, Photo, models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class TruckForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'multiple': 'true', 'label': 'photo_album'}))
    class Meta:
        model = Truck_card
        fields = ["truck_name", "truck_year", "mileage_in_km", "location", "price", "photo", "HP", "torque", "weight", "max_speed", "fuel_tank", "lifting_capacity", "description"]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["photo"]

class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'input', 'placeholder':'example@gmail.com'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("password don't match")
        return cd['password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']






