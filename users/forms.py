# users/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import Profile, User


#### Admin ####
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


#### User Forms ####
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("email",)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "tag",
            "bio",
            "profile_image",
        )
