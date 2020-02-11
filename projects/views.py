from django.shortcuts import render, redirect, reverse
from django.views import generic
from .validator import check_email
from django.http import HttpResponseRedirect, Http404

from .models import Project, Message
from .forms import ContactForm

from django.shortcuts import render_to_response


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    # Get contact form (name, email, message)
    form_class = ContactForm

    # If the submit button was pressed, proceed
    # Else return blank form
    if request.method == 'POST':
        form = form_class(data=request.POST)  # ...extract the data from the request into 'form'

        #
        #                         HttpRequest.POST
        # A dictionary-like object containing all given HTTP POST parameters,
        #           providing that the request contains form data.
        #
        #                       dict.get(key, value)
        # The get() method returns the value for the specified key if key is
        #                          in dictionary.
        #

        # If the content of the form (extracted data) is valid (input meets form requirements) proceed
        # Else render blank form
        if form.is_valid():
            name = request.POST.get('name', '')  # ...extract the name
            email = request.POST.get('email', '')  # ...extract the email
            message = request.POST.get('message', '')  # ...extract the message

            # Verify if the name variable contains only letters - if not, return alert
            if not name.isalpha():
                return render(request, 'contact.html', {'form': form_class, 'alert': 'I guess it is not your real name'})

            # If a message in the database with this email already exists, return alert
            # Else proceed
            if Message.objects.filter(email=email).exists():
                return render(request, 'contact.html', {'form': form_class, 'alert': 'You have messaged me already.'})
            else:
                # If the email is valid, save the message to the database
                # Else return alert
                if check_email(email):
                    email_message = Message(name=name, email=email,
                                            message=message)  # Add gathered data to the model instance
                    email_message.save()  # Save it to database

                    request.session['pp_contact'] = True
                    return HttpResponseRedirect(reverse('contact-success'))  # Get the user to the contact-success page
                else:
                    return render(request, 'contact.html', {'form': form_class, 'alert': 'Address email is invalid or cannot be verified.'})

    # Return (render) contact page with form_class as form (context)
    return render(request, 'contact.html', {'form': form_class})


def contact_success(request):
    if 'pp_contact' in request.session:
        del request.session['pp_contact']
        return render(request, 'contact_success.html')
    raise Http404


class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project


def handler404(request, exception, template_name="errors/404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, template_name="errors/500.html"):
    response = render_to_response(template_name)
    response.status_code = 500
    return response


def handler403(request, exception, template_name="errors/403.html"):
    response = render_to_response(template_name)
    response.status_code = 403
    return response


def handler400(request, exception, template_name="errors/400.html"):
    response = render_to_response(template_name)
    response.status_code = 400
    return response
