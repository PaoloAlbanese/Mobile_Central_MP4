from django import forms


# We're in ContactUs forms.

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50, required=True)
    name = forms.CharField(max_length=20, required=True)
    from_email = forms.EmailField(max_length=50, required=True)
    
    message = forms.CharField(
        max_length=1500,
        required=True,
        widget=forms.Textarea(),
        help_text="",
    )

class AuthContactForm(forms.Form):
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(
        max_length=1500,
        required=True,
        widget=forms.Textarea(),
        help_text="",
    )    