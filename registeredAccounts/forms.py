from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg youremail@here.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2', 'email')

# class AuthContactForm(forms.Form):
#     subject = forms.CharField(max_length=50, required=True)
#     message = forms.CharField(
#         max_length=500,
#         required=True,
#         widget=forms.Textarea(),
#         help_text="",
#     )

