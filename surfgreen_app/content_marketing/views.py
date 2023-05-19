# views.py
import logging

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
            # form.save()
            response_data = {"success": True, "message": "Form submitted successfully"}
        else:
            response_data = {"success": False, "errors": form.errors}
        return JsonResponse(response_data)
