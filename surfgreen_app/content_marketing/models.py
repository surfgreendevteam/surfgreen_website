from cms.models import CMSPlugin
from django.db import models


# Create your models here.
class HeroServiceModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class OfferServiceModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="offer_service_module", blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class OfferServiceItem(CMSPlugin):
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class HowWeWorkModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255, blank=True, null=True)
    link_title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class HowWeWorkItem(CMSPlugin):
    step_number = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class ContentLeftRightModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255, blank=True, null=True)
    link_title = models.CharField(max_length=255, blank=True, null=True)
    image_is_left = models.BooleanField(default=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="content_left_right_module", blank=True, null=True)

    def __str__(self):
        return self.title
