from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse

from .models import Project
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(email[0:email.find('@')], form.cleaned_data['message'])
            send_mail('New Enquiry', message, email, ['paj24@aber.ac.uk'])

            return render(request, 'sent_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project
