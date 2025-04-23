from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def home(request):
	return render(request, 'base/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                f"New Contact: {subject}",
                f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                'ahmdmadbdallhmhmd@gmail.com',  # email that send mails
                ['anaahmed1512@gmail.com'],  # my receiver email that receive mails
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('base:contact')
    else:
        form = ContactForm()
    return render(request, 'base/contact.html', {'form': form})


##############################################################################################

#   - ai-Workflow
def aiWorkflow(request):
	return render(request, 'base/ai-Workflow.html')

#   - learn-hub
def learnhub(request):
	return render(request, 'base/learn-hub.html')

#   - job-boards
def jobboards(request):
	return render(request, 'base/job-boards.html')

#   - cars-marketplace
def carsmarketplace(request):
	return render(request, 'base/cars-marketplace.html')

#   - chat-app
def chatapp(request):
	return render(request, 'base/chat-app.html')

#   - e-commerce
def ecommerce(request):
	return render(request, 'base/e-commerce.html')

#   - mario 
def mario(request):
	return render(request, 'base/mario.html')

#   - networks
def networks(request):
	return render(request, 'base/networks.html')


