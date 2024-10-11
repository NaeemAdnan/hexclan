from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.EmailInput)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username')