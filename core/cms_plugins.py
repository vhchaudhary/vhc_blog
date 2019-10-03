# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _
from .models import *
from .plugin_models import *
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
            'blogs': Blog.objects.all()[:6],
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
            'blogs': Blog.objects.all()[:6],
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
            'blogs': Blog.objects.all()[:4],
        })
        return context


plugin_pool.register_plugin(CMSHomeFeaturedPostPlugin)


class CMSHomeCategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    name = _('Blog Categories')
    render_template = 'cms_plugins/home/category.html'

    def render(self, context, instance, placeholder):
        context.update({
            'categories': [{'id': ct.id,
                            'name': ct.name,
                            'count': Blog.objects.filter(tech__category__pk=ct.id).count()}
                           for ct in Category.objects.all()]})
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'technologies': Technology.objects.all()
        })
        return context


plugin_pool.register_plugin(CMSHomeCategoryPlugin)


def get_last_six_months():
    months = []
    today = datetime.today()
    for i in range(1, 7):
        months.append((today.strftime('%B'), today.year))
        today = today - relativedelta(months=1)
    return months


class CMSPostArchivePlugin(CMSPluginBase):
    model = PostArchivePlugin
    name = _('Post Archive')
    render_template = 'cms_plugins/post/archive.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'months': get_last_six_months()
        })
        return context


plugin_pool.register_plugin(CMSPostArchivePlugin)


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


class CMSPostContentPlugin(CMSPluginBase):
    model = PostContentPlugin
    name = _("Post Content")
    render_template = 'cms_plugins/post/content.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSPostContentPlugin)


class CMSPostHeaderPlugin(CMSPluginBase):
    model = PostHeaderPlugin
    name = _("Post Header")
    render_template = 'cms_plugins/post/post_header.html'

    def render(self, context, instance, placeholder):
        current_page = context.get('request').current_page.get_title()
        blog = Blog.objects.get(title=current_page)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'blog': blog,
        })
        return context


plugin_pool.register_plugin(CMSPostHeaderPlugin)


class CMSPostAuthorPlugin(CMSPluginBase):
    model = PostAuthorPlugin
    name = _("Post Author")
    render_template = 'cms_plugins/post/author.html'

    def render(self, context, instance, placeholder):
        current_page = context.get('request').current_page.get_title()
        author = Blog.objects.get(title=current_page).author
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'author': author,
        })
        return context


plugin_pool.register_plugin(CMSPostAuthorPlugin)


class CMSPostCommentPlugin(CMSPluginBase):
    model = PostCommentPlugin
    name = _("Post Comment")
    render_template = 'cms_plugins/post/comment.html'

    def render(self, context, instance, placeholder):
        current_page = context.get('request').current_page.get_title()
        blog = Blog.objects.get(title=current_page)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'blog': blog,
        })
        return context


plugin_pool.register_plugin(CMSPostCommentPlugin)


class PostSearchListPlugin(CMSPluginBase):
    model = PostSearchList
    name = _("Post Search List")
    render_template = 'cms_plugins/post_list/post_search_list.html'

    def render(self, context, instance, placeholder):
        id = context.get('request').GET.get('id')
        month = context.get('request').GET.get('month')
        year = context.get('request').GET.get('year')
        if id:
            blogs = Blog.objects.filter(tech__category__pk=id)
        elif month and year:
            month_no = int(datetime.strptime(month, '%B').strftime('%m'))
            blogs = Blog.objects.filter(modified__year=year, modified__month=month_no)

        context.update({
            'blogs': blogs
        })
        return context


plugin_pool.register_plugin(PostSearchListPlugin)
