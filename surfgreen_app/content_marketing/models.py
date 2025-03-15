from cms.models import CMSPlugin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


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
    short_description = HTMLField(blank=True, null=True)
    course_description = HTMLField(blank=True, null=True)
    course_image = models.ImageField(upload_to="course_detail", blank=True, null=True)
    course_image_title = models.CharField(max_length=255, blank=True, null=True)
    course_image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    course_author = models.CharField(max_length=255, blank=True, null=True)
    course_author_description = HTMLField(blank=True, null=True)
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


class CourseOverviewModul(CMSPlugin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CourseOverviewItem(CMSPlugin):
    title = models.CharField(max_length=255)
    course_author = models.CharField(max_length=255)
    link = models.CharField(
        max_length=255,
        help_text="Enter link to the course detail page for the specific course",
    )
    link_title = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.PositiveIntegerField(
        blank=True, null=True, help_text="Enter the duration of the course in hours."
    )
    course_image = models.ImageField(upload_to="course_overview", blank=True, null=True)
    course_image_title = models.CharField(max_length=255, blank=True, null=True)
    course_image_alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class AppLandingHeroModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    hero_mockup_image_1 = models.ImageField(upload_to="app_landing", blank=True, null=True)
    hero_mockup_image_2 = models.ImageField(upload_to="app_landing", blank=True, null=True)
    apple_app_store_link = models.CharField(max_length=255, blank=True, null=True)
    play_store_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class AppLandingFeatureModule(CMSPlugin):
    features_title = models.CharField(
        max_length=255, blank=True, null=True, help_text="The heading for the features section"
    )
    features_description = models.TextField(
        blank=True,
        null=True,
        help_text="The description for the features section. For single feature add feature plugin",
    )
    features_phone_image = models.ImageField(upload_to="app_features", blank=True, null=True)

    def __str__(self):
        return self.features_title


class AppLandingFeatureItem(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to="app_landing_feature_item", blank=True, null=True)

    def __str__(self):
        return self.title


class AppLandingHowDoesItWorkModule(CMSPlugin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AppLandingHowDoesItWorkScreenItem(CMSPlugin):
    screen_image = models.ImageField(upload_to="app_landing_how_does_it_work", blank=True, null=True)
    data_swiper_slide_index = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "data_swiper_slide_index_" + str(self.data_swiper_slide_index)


class AppLandingHowDoesItWorkTextItem(CMSPlugin):
    data_swiper_slide_index = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    data_swiper_slide_index = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class AppLandingFaqModule(CMSPlugin):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True, help_text="The text below title for the faq section")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.title


class AppLandingFaqItem(CMSPlugin):
    question_number = models.PositiveIntegerField(
        help_text="The number of the question, important for the data-toggle"
    )
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class AppLandingTestimonialsModule(CMSPlugin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AppLandingTestimonialsItem(CMSPlugin):
    stars = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="The number of stars for the testimonial 0-5(5 is the best)",
    )
    testimonial_text = models.TextField(max_length=360)
    testimonial_author = models.CharField(max_length=255)
    testimonial_author_role = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "testimonial of " + self.testimonial_author


class HomePageHeroModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sub_1 = models.CharField(max_length=255)
    sub_2 = models.CharField(max_length=255)
    sub_3 = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class HomepageAboutModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="offer_service_module", blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class PricingContainerModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class PricingItem(CMSPlugin):
    title = models.CharField(max_length=255)
    is_highlighted = models.BooleanField(default=False)
    image = models.ImageField(upload_to="pricing_item", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    

class PricingFeatureItem(CMSPlugin):
    title = models.CharField(max_length=255)
    included = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class WebdesignHeroModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    
class WebdesignHeroImage(CMSPlugin):
    image = models.ImageField(upload_to="webdesign_hero_image", blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image_title
    

class LogoContainerModule(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class LogoItem(CMSPlugin):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="logo_item", blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.id)