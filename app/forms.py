from django import forms
import csv
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from app.models import Test_Suite



class BootstrapAuthenticationForm(AuthenticationForm):
    
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   "class": "form-control",
                                   "placeholder": "User name"}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   "class": "form-control",
                                   "placeholder":"Password"}))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class TestSuiteForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the title of the page.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Test_Suite
        fields = ("Test_Suite_Name",)


DISPLAY_CHOICES = (
    ("1", "REG_AGREED_SUITE01"),
    ("2", "REG_AGREED_SUITE02")
)

class RevoForm(forms.ModelForm):
    class Meta:
      model = Test_Suite
      fields = ['Test_Suite_Name']
    # checks = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)