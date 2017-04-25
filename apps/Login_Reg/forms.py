from django import forms
# does import forms grab ModelForm?
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""
TODO for Login_Reg: forms.py
- Modify auth to use bcrypt vs default django encrypt
- Possibly modify/extend Django forms to show understanding
"""
## Model-based forms
## Extending the Django UserCreationForm class
## UserCreateForm is a subclass of UserCreationForm
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "password1","password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

## Forms
## Extending the Django AuthenticationForm class
## LoginForm is a subclass of AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(label=
    'username', max_length=45)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
