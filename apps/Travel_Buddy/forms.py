from django import forms
# does import forms grab ModelForm?
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Trips


"""
TODO for Book_Reviews: forms.py
-
"""
## Model-based forms
## Extending the Django UserCreationForm class
## UserCreateForm is a subclass of UserCreationForm
class TripCreateForm(forms.ModelForm):
    # title = forms.CharField(max_length=256, required=True)
    # author = forms.CharField(max_length=128, required=True)
    travel_start = forms.DateField(widget=forms.SelectDateWidget())
    travel_end = forms.DateField(widget=forms.SelectDateWidget())
    prefix = 'trip'
    class Meta:
        model = Trips
        fields = ['destination', 'description',]

    def save(self,user_id,commit=True):
        trip = super(TripCreateForm, self).save(commit=False)
        trip.destination = self.cleaned_data["destination"]
        trip.description = self.cleaned_data["description"]
        trip.travel_start = self.cleaned_data["travel_start"]
        trip.travel_end = self.cleaned_data["travel_end"]
        trip.user_id = user_id
        if commit:
            trip.save()
        return trip

    def process_traveler(self, traveler_to_add):
        trip = super(TripCreateForm, self).save(commit=False)
        trip.travelers = traveler_to_add.id
        trip.save()
        return trip



## Forms
## Extending the Django AuthenticationForm class
## LoginForm is a subclass of AuthenticationForm
