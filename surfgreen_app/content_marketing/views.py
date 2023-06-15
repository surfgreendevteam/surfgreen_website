# views.py
import logging

from django.core.mail import mail_admins
from django.http import JsonResponse
from django.views import View

from .forms import ContactForm as MyForm

logger = logging.getLogger(__name__)


class ContactFormAjaxView(View):
    form_class = MyForm

    def get(self, request):
        form = self.form_class()
        return JsonResponse({"form": form.as_p()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process the form data here
            # Example: Save the form data to a database
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            service = form.cleaned_data["service"]
            subject = "Contact Form Message from Surfgreen Website"

            message = f"<p>Name: {name}</p><p>Email: {email}</p><p>Message: {message}</p><p>Service: {service}</p>"

            mail_admins(subject, message, fail_silently=True, html_message=message)

            response_data = {"success": True, "message": "Form submitted successfully"}
        else:
            response_data = {"success": False, "errors": form.errors}
        return JsonResponse(response_data)
