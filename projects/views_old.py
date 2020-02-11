from django.shortcuts import render, redirect
from django.views import generic
from django.template.loader import get_template
from django.core.mail import EmailMessage

from .models import Project
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    # Get contact form (name, email, message)
    form_class = ContactForm

    if request.method == 'POST':    # If the submit button was pressed...
        form = form_class(data=request.POST)    # ...extract the data from the request into 'form'

        #
        #                         HttpRequest.POST
        # A dictionary-like object containing all given HTTP POST parameters,
        #           providing that the request contains form data.
        #
        #                       dict.get(key, value)
        # The get() method returns the value for the specified key if key is
        #                          in dictionary.
        #
        # email = EmailMessage(
        #     subject=      'Hello',
        #     body=         'Body goes here',
        #     from_email=   'from@example.com',
        #     to=           ['to1@example.com', 'to2@example.com'],
        #     bcc=          ['bcc@example.com'],
        #     reply_to=     ['another@example.com'],
        #     headers=      {'Message-ID': 'foo'},
        # )
        #
        if form.is_valid():     # If the content of the form (extracted data) is valid...
            name = request.POST.get('name', '')     # ...extract the name
            email = request.POST.get('email', '')    # ...extract the email
            message = request.POST.get('message', '')   # ...extract the message

            # Email the profile with the contact information
            template = get_template('contact_template.txt')     # Grab template for message output
            context = {
                'name': name,
                'email': email,
                'message': message,
            }   # Organise user input into context dictionary
            content = template.render(context)  # Feed context into contact_template

            email_message = EmailMessage(
                subject='New message.',
                body=content,
                from_email=email,
                to=['robermaselko@gmail.com'],
                headers={'Reply-To': email}
            )   # Build a message
            email_message.send()    # And send it
            return redirect('contact')  # Get the user back to the contact page

    # Return (render) contact page with form_class as form (context)
    return render(request, 'contact.html', {'form': form_class})


class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project
