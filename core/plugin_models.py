
from cms.models import CMSPlugin
from django.db import models
# from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _


class HomeBannerPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=250, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class RecentPostPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class FeaturedPostPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class MostReadPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class CategoryPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class PostArchivePlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class PostHeaderPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class PostAuthorPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class AdBanner300X250(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    link = models.URLField(_("Link"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')


class AdBanner728X90(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    link = models.URLField(_("Link"), max_length=200, blank=True, default='')
    description = models.CharField(_('Description'), max_length=500, blank=True, default='')