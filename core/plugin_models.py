
from cms.models import CMSPlugin
from django.db import models
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _


class HomeBannerPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=250, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class RecentPostPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class FeaturedPostPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class MostReadPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class CategoryPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class PostArchivePlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class PostHeaderPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class PostContentPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = RedactorField(_('Description'), blank=True, default='')


class PostAuthorPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class PostCommentPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class AdBanner300X250(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    client_id = models.CharField(_("Client ID"), max_length=200, blank=True, default='')
    slot = models.CharField(_("Slot"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class AdBanner728X90(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    client_id = models.CharField(_("Client ID"), max_length=200, blank=True, default='')
    slot = models.CharField(_("Slot"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class PostSearchList(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')


class PluginNewsLetter(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, blank=True, default='')
    description = models.TextField(_('Description'), max_length=500, blank=True, default='')
    linked_in_link = models.URLField(_("LinkedIn Link"), null=True, blank=True, )
    facebook_link = models.URLField(_("Facebook Link"), null=True, blank=True, )
    twitter_link = models.URLField(_("Twitter Link"), null=True, blank=True, )
    google_link = models.URLField(_("Google Link"), null=True, blank=True, )
    instagram_link = models.URLField(_("Instagram Link"), null=True, blank=True, )
