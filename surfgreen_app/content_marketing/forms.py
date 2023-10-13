from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    service = forms.ChoiceField(
        label=_("Service"),
        choices=[
            ("django", _("Python Django")),
            ("onetausend", _("1.000 Euro Webseite")),
            ("green", _("Green Web Development")),
            ("training", _("Python Django Training")),
            ("outsourcing", _("Developer Outsourcing")),
            ("consulting", _("Beratung")),
            ("other", _("Other")),
        ],
    )
    name = forms.CharField(label=_("Ihr Name"), max_length=100)
    email = forms.EmailField(label=_("Ihre E-Mail"), max_length=100)
    message = forms.CharField(label=_("Ihre Nachricht"), max_length=1000, widget=forms.Textarea)
    data_privacy = forms.BooleanField(
        label=mark_safe(
            _("Ich habe die <a href='/datenschutz'>Datenschutzerklärung</a> gelesen und akzeptiere diese.")
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_tag = False
        self.helper.layout = Layout(
            "service", "name", "email", "message", Submit("submit", _("Senden"), css_class="btn btn-primary")
        )
