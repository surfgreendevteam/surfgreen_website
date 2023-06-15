from django.urls import path

from surfgreen_app.content_marketing.views import ContactFormAjaxView

app_name = "content_marketing"

urlpatterns = [
    path(
        "~contact/",
        view=ContactFormAjaxView.as_view(),
        name="contact_form",
    ),
]
