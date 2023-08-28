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


class WhyChooseUsModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class WhyChooseUsItem(CMSPlugin):
    icon = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)


class GetInTouchModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email_adress = models.CharField(max_length=255, blank=True, null=True)
    street_adress = models.CharField(max_length=255, blank=True, null=True)
    city_adress = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class FooterModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email_adress = models.CharField(max_length=255, blank=True, null=True)
    street_adress = models.CharField(max_length=255, blank=True, null=True)
    city_adress = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    seo_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class NavbarModule(CMSPlugin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CourseDetail(CMSPlugin):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.PositiveIntegerField(
        blank=True, null=True, help_text="Enter the duration of the course in hours."
    )
    short_description = models.TextField(blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    course_image = models.ImageField(upload_to="course_detail", blank=True, null=True)
    course_image_title = models.CharField(max_length=255, blank=True, null=True)
    course_image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    course_author = models.CharField(max_length=255, blank=True, null=True)
    course_author_description = models.TextField(blank=True, null=True)
    course_author_image = models.ImageField(upload_to="course_author", blank=True, null=True)
    course_author_image_title = models.CharField(max_length=255, blank=True, null=True)
    course_author_image_alt_text = models.CharField(max_length=255, blank=True, null=True)

    #  course_author_linkedin = models.CharField(max_length=255, blank=True, null=True)  for later
    def __str__(self):
        return self.title


class CourseDetailContent(CMSPlugin):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class CourseDetailWhatYouLearnItem(CMSPlugin):
    description = models.TextField()

    def __str__(self):
        return self.description
