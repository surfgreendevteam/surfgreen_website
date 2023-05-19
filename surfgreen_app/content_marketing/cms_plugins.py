from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from surfgreen_app.content_marketing.models import (
    HeroServiceModule,
    HowWeWorkItem,
    HowWeWorkModule,
    OfferServiceItem,
    OfferServiceModule,
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
