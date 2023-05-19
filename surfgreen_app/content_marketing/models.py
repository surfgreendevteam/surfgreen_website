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
