from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    service = forms.ChoiceField(
        label=_("Service"),
        choices=[("django", _("Python Django")), ("consulting", _("Beratung")), ("other", _("Other"))],
    )
    name = forms.CharField(label=_("Ihr Name"), max_length=100)
    email = forms.EmailField(label=_("Ihre E-Mail"), max_length=100)
    message = forms.CharField(label=_("Ihre Nachricht"), max_length=1000, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "service", "name", "email", "message", Submit("submit", _("Senden"), css_class="btn btn-primary")
        )
