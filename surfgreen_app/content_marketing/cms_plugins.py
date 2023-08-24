from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from surfgreen_app.content_marketing.forms import ContactForm
from surfgreen_app.content_marketing.models import (
    ContentLeftRightModule,
    FooterModule,
    GetInTouchModule,
    HeroServiceModule,
    HowWeWorkItem,
    HowWeWorkModule,
    OfferServiceItem,
    OfferServiceModule,
    WhyChooseUsItem,
    WhyChooseUsModule,
    NavbarModule,
    CourseDetail,
    CourseDetailContent,
    CourseDetailWhatYouLearnItem,
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
    modul = _("Navbar Module")
    name = _("Navbar Module Plugin")
    render_template = "content_marketing/navbar.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseDetailPublisher(CMSPluginBase):
    model = CourseDetail
    modul = _("Course Detail Module")
    name = _("Course Detail Module Plugin")
    render_template = "content_marketing/course_detail.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseContentPublisher(CMSPluginBase):
    model = CourseDetailContent
    modul = _("Course Content Module")
    name = _("Course Content Module Plugin")
    render_template = "content_marketing/course_content.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class CourseWhatYouLearnPublisher(CMSPluginBase):
    model = CourseDetailWhatYouLearnItem
    modul = _("Course What You Learn Module")
    name = _("Course What You Learn Module Plugin")
    render_template = "content_marketing/course_what_you_learn_item.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
