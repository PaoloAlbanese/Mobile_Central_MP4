# from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from .forms import AuthContactForm, ContactForm
from django.core.mail import send_mail
from mailjet_rest import Client
import os
from django import template
import datetime
from time import gmtime, strftime
from django.utils import dateformat, formats, timezone


# We're in contactUs views.


def contact(request):
    emailJSidMM = settings.EMAILJS_USER_MM
    # emailJSid = ""
    emailJSsendMessage = settings.EMAILJS_SENDMSG
    # emailJSsendMessage=""
    dTime = datetime.datetime.now().date
    # eTime=dTime.strftime("%Y-%m-%d %H:%M:%S")
    eMessage=""
    eSubject=""
    captName=""
    from_email=""

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
            # eTime = datetime
            # print('eTime',eTime)

            # subject = eSubject
            # message = eMessage

            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = ['paulitus_@hotmail.com',]

            # send_mail( subject, message, email_from, recipient_list),
            # return render(request, 'contactUs/contact_success.html', {'message': message, 'name': captName, 'emailTo': from_email, 'subject': subject, 'emailJSid': emailJSid})
            # print('eTime',eTime)
            print('eMessage',eMessage)
            print('eSubject',eSubject)

            return render(request, 'contactUs/contact_success.html', {'message': eMessage, 'name': captName, 'emailTo': from_email, 'subject': eSubject, 'emailJSidMM': emailJSidMM,'emailJSsendMessage':emailJSsendMessage,})

    else:
        if request.user.is_authenticated:
            form = AuthContactForm()
        else:
            form = ContactForm()
    
    # now=datetime.datetime.now()
    # eTime=str("etime is: "+ now.strftime("%d-%b-%Y") + " at " + now.strftime("%H:%M:%S"))
    # print(eTime)
    # print("Date is: "+ now.strftime("%Y-%m-%d"))
    # print("Date is: "+ now.strftime("%d-%b-%Y") + " at " + now.strftime("%H:%M:%S")) #this will print **2018-02-01** that is todays date


    # api_key = 'f3afd5c712e2a861966c4fa4e58be6b0'
    # api_secret = 'd88604054ab22dbd591f4ae99d101a7e'
    # mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    # data = {
    #     'Messages': [
    #         {
    #             "From": {
    #                 "Email": "paulitus_@hotmail.com",
    #                 "Name": "paolo"
    #             },
    #             "To": [
    #                 {
    #                     "Email": "paulitus_@hotmail.com",
    #                     "Name": "paolo"
    #                 }
    #             ],
    #             "Subject": "Greetings from Mailjet.",
    #             "TextPart": "My first Mailjet email",
    #             "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
    #             "CustomID": "AppGettingStartedTest"
    #         }
    #     ]
    # }
    # result = mailjet.send.create(data=data)
    # print ('result staus code',result.status_code)
    # print ('json result',result.json())

    return render(request, 'contactUs/contact.html', {'form': form})
