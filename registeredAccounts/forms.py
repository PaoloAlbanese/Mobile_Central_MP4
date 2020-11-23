from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# We're in registeredAccounts forms.


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg youremail@here.com')

    """'
    from https://stackoverflow.com/questions/7948750/
                        custom-form-validation/7948998,
    the default django user does not require a unique email address (!?!)
    """
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2', 'email')
