from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from surfgreen_app.content_marketing.forms import ContactForm
from surfgreen_app.content_marketing.models import (
    AppLandingFaqItem,
    AppLandingFaqModule,
    AppLandingFeatureItem,
    AppLandingFeatureModule,
    AppLandingHeroModule,
    AppLandingHowDoesItWorkModule,
    AppLandingHowDoesItWorkScreenItem,
    AppLandingHowDoesItWorkTextItem,
    AppLandingTestimonialsItem,
    AppLandingTestimonialsModule,
    ContentLeftRightModule,
    CourseDetail,
    CourseDetailContent,
    CourseDetailWhatYouLearnItem,
    CourseOverviewItem,
    CourseOverviewModul,
    FooterModule,
    GetInTouchModule,
    HeroServiceModule,
    HomepageAboutModule,
    HomePageHeroModule,
    HowWeWorkItem,
    HowWeWorkModule,
    NavbarModule,
    OfferServiceItem,
    OfferServiceModule,
    WhyChooseUsItem,
    WhyChooseUsModule,
    PricingContainerModule,
    PricingItem,
    PricingFeatureItem
)


@plugin_pool.register_plugin  # register the plugin
class HeroServiceModulePublisher(CMSPluginBase):
    model = HeroServiceModule  # model where plugin data are saved
    module = _("Hero Service Module")
    name = _("Hero Service Module Plugin")  # name of the plugin in the interface
    render_template = "content_marketing/hero_service_module.html"

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context


@plugin_pool.register_plugin  # register the plugin
class HomePageHeroModulePublisher(CMSPluginBase):
    model = HomePageHeroModule  # model where plugin data are saved
    module = _("Home Page Hero Module")
    name = _("Home Page Hero Plugin")  # name of the plugin in the interface
    render_template = "content_marketing/homepage_hero.html"

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context


@plugin_pool.register_plugin  # register the plugin
class HomePageAboutModulePublisher(CMSPluginBase):
    model = HomepageAboutModule  # model where plugin data are saved
    module = _("Home Page About Module")
    name = _("Home Page About Plugin")  # name of the plugin in the interface
    render_template = "content_marketing/homepage_about_module.html"

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context


@plugin_pool.register_plugin
class OfferServiceModulePublisher(CMSPluginBase):
    model = OfferServiceModule
    module = _("Offer Service Module")
    name = _("Offer Service Module Plugin")
    render_template = "content_marketing/offer_service_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class OfferServiceItemPublisher(CMSPluginBase):
    model = OfferServiceItem
    module = _("Offer Service Item")
    name = _("Offer Service Item Plugin")
    render_template = "content_marketing/offer_service_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class HowWeWorkModulePublisher(CMSPluginBase):
    model = HowWeWorkModule
    module = _("How we work Module")
    name = _("How we work Module Plugin")
    render_template = "content_marketing/howwework_service_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class HowWeWorkItemPublisher(CMSPluginBase):
    model = HowWeWorkItem
    module = _("How we work Item")
    name = _("How we work Item Plugin")
    render_template = "content_marketing/howwework_service_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ContentLeftRightModulePublisher(CMSPluginBase):
    model = ContentLeftRightModule
    module = _("Content Left Right Module")
    name = _("Content Left Right Module Plugin")
    render_template = "content_marketing/content_left_right_module.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class WhyChooseUsModulePublisher(CMSPluginBase):
    model = WhyChooseUsModule
    module = _("Why Choose Us Module")
    name = _("Why Choose Us Module Plugin")
    render_template = "content_marketing/why_choose_us_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class WhyChooseUsItemPublisher(CMSPluginBase):
    model = WhyChooseUsItem
    module = _("Why Choose Us Item")
    name = _("Why Choose Us Item Plugin")
    render_template = "content_marketing/why_choose_us_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class GetInTouchModulePublisher(CMSPluginBase):
    model = GetInTouchModule
    module = _("Get In Touch Module")
    name = _("Get In Touch Module Plugin")
    render_template = "content_marketing/get_in_touch.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        form = ContactForm()
        context.update({"form": form})
        return context


@plugin_pool.register_plugin
class FooterModulePublisher(CMSPluginBase):
    model = FooterModule
    module = _("Footer Module")
    name = _("Footer Module Plugin")
    render_template = "content_marketing/footer.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class NavbarModulPublisher(CMSPluginBase):
    model = NavbarModule
    module = _("Navbar Module")
    name = _("Navbar Module Plugin")
    render_template = "content_marketing/navbar.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseDetailPublisher(CMSPluginBase):
    model = CourseDetail
    module = _("Course Detail Module")
    name = _("Course Detail Module Plugin")
    render_template = "content_marketing/course_detail.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseContentPublisher(CMSPluginBase):
    model = CourseDetailContent
    module = _("Course Detail Module")
    name = _("Course Content Module Plugin")
    render_template = "content_marketing/course_content.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseWhatYouLearnPublisher(CMSPluginBase):
    model = CourseDetailWhatYouLearnItem
    module = _("Course Detail Module")
    name = _("Course What You Learn Module Plugin")
    render_template = "content_marketing/course_what_you_learn_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseOverviewModulPublisher(CMSPluginBase):
    model = CourseOverviewModul
    module = _("Course Overview Module")
    name = _("Course Overview Module Plugin")
    render_template = "content_marketing/course_overview.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseOverviewItemPublisher(CMSPluginBase):
    model = CourseOverviewItem
    module = _("Course Overview Item")
    name = _("Single Course Item for Overview")
    render_template = "content_marketing/course_overview_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingHeroModulePublisher(CMSPluginBase):
    model = AppLandingHeroModule
    module = _("App Landing Hero Module")
    name = _("App Landing Hero Module Plugin")
    render_template = "content_marketing/app_landing_hero_module.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingFeatureModulePublisher(CMSPluginBase):
    model = AppLandingFeatureModule
    module = _("App Landing Feature Module")
    name = _("App Landing Feature Module Plugin")
    render_template = "content_marketing/app_landing_feature_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingFeatureItemPublisher(CMSPluginBase):
    model = AppLandingFeatureItem
    module = _("App Landing Feature Item")
    name = _("App Landing Feature Item Plugin")
    render_template = "content_marketing/app_landing_feature_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class HowDoesItWorkModulePublisher(CMSPluginBase):
    model = AppLandingHowDoesItWorkModule
    module = _("App How Does it Work Module")
    name = _("App How Does it Work Module Plugin")
    render_template = "content_marketing/app_landing_how_does_it_work_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingHowDoesItWorkScreenItemPublisher(CMSPluginBase):
    model = AppLandingHowDoesItWorkScreenItem
    module = _("App How Does it Work Module")
    name = _("App How Does it Work Screen Item Plugin")
    render_template = "content_marketing/app_landing_how_does_it_work_screen_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingHowDoesItWorkTextItemPublisher(CMSPluginBase):
    model = AppLandingHowDoesItWorkTextItem
    module = _("App How Does it Work Module")
    name = _("App How Does it Work Text Item Plugin")
    render_template = "content_marketing/app_landing_how_does_it_work_text_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingFaqModulePublisher(CMSPluginBase):
    model = AppLandingFaqModule
    module = _("App FAQ Module")
    name = _("App FAQ Module Plugin")
    render_template = "content_marketing/app_landing_faq_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingFaqItemPublisher(CMSPluginBase):
    model = AppLandingFaqItem
    module = _("App FAQ Module")
    name = _("App FAQ Item Plugin")
    render_template = "content_marketing/app_landing_faq_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingTestimonialsModulePublisher(CMSPluginBase):
    model = AppLandingTestimonialsModule
    module = _("App Testimonials Module")
    name = _("App Testimonials Module Plugin")
    render_template = "content_marketing/app_landing_testimonials_module.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class AppLandingTestimonialsItemPublisher(CMSPluginBase):
    model = AppLandingTestimonialsItem
    module = _("App Testimonials Module")
    name = _("App Testimonials Item Plugin")
    render_template = "content_marketing/app_landing_testimonials_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class PricingContainerModulePublisher(CMSPluginBase):
    model = PricingContainerModule
    module = _("Pricing Container Module")
    name = _("Pricing Container Module Plugin")
    render_template = "content_marketing/pricing_container_module.html"
    allow_children = True
    

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
    
@plugin_pool.register_plugin
class PricingItemPublisher(CMSPluginBase):
    model = PricingItem
    module = _("Pricing Item")
    name = _("Pricing Item Plugin")
    render_template = "content_marketing/pricing_item.html"
    require_parent = True
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
    
@plugin_pool.register_plugin
class PricingFeatureItemPublisher(CMSPluginBase):
    model = PricingFeatureItem
    module = _("Pricing Feature Item")
    name = _("Pricing Feature Item Plugin")
    render_template = "content_marketing/pricing_feature_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context