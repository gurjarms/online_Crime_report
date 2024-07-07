# noinspection PyUnresolvedReferences
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserVarify, Profile, UserMobileNo
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={}))
    Mobile_No = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'Mobile_No', 'password1', 'password2'
        ]


class UserVaryfyForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True)


class ProfileUpdateForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            return cleaned_data
        ...
        return cleaned_data

    class Meta:
        model = Profile
        fields = ['image']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
