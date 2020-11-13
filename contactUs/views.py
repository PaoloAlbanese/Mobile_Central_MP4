from django.shortcuts import render
from django.conf import settings
from .forms import AuthContactForm, ContactForm

# We're in contactUs views.

def contact(request):
    emailJSid= settings.EMAILJS_USER_ID
    # emailJSsendMessage = settings.EMAILJS_SIGNUP

    
    if request.method=="POST":
        if request.user.is_authenticated:
            form=AuthContactForm(request.POST)
        else:
            form=ContactForm(request.POST)
        subject=""
        message=""
        if form.is_valid():


            if request.user.is_authenticated: 
                name = request.user.first_name
                from_email = request.user.email
                captName = name.title()
                
            else:
                from_email= form.cleaned_data.get('from_email')
                name= form.cleaned_data.get('name')
                captName = name.title()
                

            message= form.cleaned_data.get('message')    
            subject= form.cleaned_data.get('subject')

            return render(request, 'contactUs/contact_success.html',{'message':message,'name':captName, 'emailTo':from_email,'subject':subject,'emailJSid':emailJSid})

    else:
        if request.user.is_authenticated:
            form = AuthContactForm()
        else:
            form= ContactForm()
    return render(request, 'contactUs/contact.html', {'form':form})