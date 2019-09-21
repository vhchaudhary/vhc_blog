# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _
from .models import *
from .plugin_models import *


class CMSHomeGallaryPlugin(CMSPluginBase):
    model = HomeBannerPlugin
    name = _('Home Gallery')
    render_template = 'cms_plugins/home/banner.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'blogs': Blog.objects.all()[:2],
        })
        return context


plugin_pool.register_plugin(CMSHomeGallaryPlugin)


class CMSHomeRecentPostPlugin(CMSPluginBase):
    model = RecentPostPlugin
    name = _('Recent Posts')
    render_template = 'cms_plugins/home/recent_post.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSHomeRecentPostPlugin)


class CMSHomeMostReadPlugin(CMSPluginBase):
    model = MostReadPlugin
    name = _('Most Readed Posts')
    render_template = 'cms_plugins/home/most_read.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSHomeMostReadPlugin)


class CMSHomeFeaturedPostPlugin(CMSPluginBase):
    model = FeaturedPostPlugin
    name = _('Featured Posts')
    render_template = 'cms_plugins/home/featured_post.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSHomeFeaturedPostPlugin)


class CMSHomeCategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    name = _('Blog Categories')
    render_template = 'cms_plugins/home/category.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'categories': Category.objects.all(),
            'technologies': Technology.objects.all()
        })
        return context


plugin_pool.register_plugin(CMSHomeCategoryPlugin)


class AdBanner300X250Plugin(CMSPluginBase):
    model = AdBanner300X250
    name = _("Ad Banner 300x250")
    render_template = 'cms_plugins/ads/ad_300x250.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(AdBanner300X250Plugin)


class AdBanner728X90Plugin(CMSPluginBase):
    model = AdBanner728X90
    name = _("Ad Banner 728x90")
    render_template = 'cms_plugins/ads/ad_728x90.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(AdBanner728X90Plugin)
