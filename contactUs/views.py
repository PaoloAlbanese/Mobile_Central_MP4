from django.shortcuts import render
from django.conf import settings
from .forms import AuthContactForm, ContactForm
from django.core.mail import send_mail
from mailjet_rest import Client
import os

# We're in contactUs views.


def contact(request):
    # emailJSid = settings.EMAILJS_USER_ID
    emailJSid = ""
    emailJSsendMessage = settings.EMAILJS_SIGNUP

    if request.method == "POST":
        if request.user.is_authenticated:
            form = AuthContactForm(request.POST)
        else:
            form = ContactForm(request.POST)
        eSubject = ""
        eMessage = ""
        if form.is_valid():

            if request.user.is_authenticated:
                name = request.user.first_name
                from_email = request.user.email
                captName = name.title()

            else:
                from_email = form.cleaned_data.get('from_email')
                name = form.cleaned_data.get('name')
                captName = name.title()

            eMessage = form.cleaned_data.get('message')
            eSubject = form.cleaned_data.get('subject')

            subject = eSubject
            message = eMessage
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['paulitus_@hotmail.com',]

            send_mail( subject, message, email_from, recipient_list ),
            return render(request, 'contactUs/contact_success.html', {'message': message, 'name': captName, 'emailTo': from_email, 'subject': subject, 'emailJSid': emailJSid})

            return render(request, 'contactUs/contact_success.html', {'message': message, 'name': captName, 'emailTo': from_email, 'subject': subject, 'emailJSid': emailJSid})

    else:
        if request.user.is_authenticated:
            form = AuthContactForm()
        else:
            form = ContactForm()

    api_key = 'f3afd5c712e2a861966c4fa4e58be6b0'
    api_secret = 'd88604054ab22dbd591f4ae99d101a7e'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "paulitus_@hotmail.com",
                    "Name": "paolo"
                },
                "To": [
                    {
                        "Email": "paulitus_@hotmail.com",
                        "Name": "paolo"
                    }
                ],
                "Subject": "Greetings from Mailjet.",
                "TextPart": "My first Mailjet email",
                "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print ('result staus code',result.status_code)
    print ('json result',result.json())

    return render(request, 'contactUs/contact.html', {'form': form})
