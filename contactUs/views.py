# from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from .forms import AuthContactForm, ContactForm

# We're in contactUs views.


def contact(request):
    emailJSidMM = settings.EMAILJS_USER_MM
    emailJSsendMessage = settings.EMAILJS_SENDMSG
    eMessage = ""
    eSubject = ""
    captName = ""
    from_email = ""

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

            return render(request, 'contactUs/contact_success.html',
                          {'message': eMessage, 'name': captName,
                           'emailTo': from_email,
                           'subject': eSubject, 'emailJSidMM': emailJSidMM,
                           'emailJSsendMessage': emailJSsendMessage, })

    else:
        if request.user.is_authenticated:
            form = AuthContactForm()
        else:
            form = ContactForm()

    return render(request, 'contactUs/contact.html', {'form': form})
