from django.core.exceptions import ValidationError
from django.db import models
from djangocms_video.models import ALLOWED_EXTENSIONS
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel
from djrichtextfield.models import RichTextField


class Category(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Categories")


class Technology(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=100)
    category = models.ForeignKey(Category, related_name='tech_ids', verbose_name=_("Category"), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Technologies")


class Author(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=50, null=True, blank=True,)
    about = models.TextField(_("About"), max_length=1000, null=True, blank=True,)
    facebook_link = models.URLField(_("Facebook Link"), null=True, blank=True,)
    twitter_link = models.URLField(_("Twitter Link"), null=True, blank=True,)
    google_link = models.URLField(_("Google Link"), null=True, blank=True,)
    instagram_link = models.URLField(_("Instagram Link"), null=True, blank=True,)
    linked_in_link = models.URLField(_("LinkedIn Link"), null=True, blank=True,)
    image = FilerImageField(verbose_name=_("Image"), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Blog(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=200)
    title = models.CharField(_("Title"), max_length=100, unique=True)
    slug = models.SlugField(_("Slug"), blank=True, default='')
    image = FilerImageField(verbose_name=_("Image"), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    small_image = FilerImageField(verbose_name=_("Small Image"), null=True, related_name='+', blank=True, on_delete=models.SET_NULL)
    video_file = FilerFileField(verbose_name=_("Video file"), null=True, blank=True, related_name='+', on_delete=models.SET_NULL,
                                help_text=_('Allowed extensions: {extension}').format(extension=ALLOWED_EXTENSIONS))
    tech = models.ForeignKey(Technology, verbose_name=_("Technology"),  on_delete=models.SET_NULL, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    content = models.TextField(_('Content'), blank=True, null=True)
    author = models.ForeignKey(Author, verbose_name=_("Author"), null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def clean(self):
        if self.video_file and self.video_file.extension not in ALLOWED_EXTENSIONS:
            raise ValidationError(_('Incorrect file type: {extension}.').format(extension=self.video_file.extension))


class Thread(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=100, unique=True)
    blog = models.ForeignKey(Blog, verbose_name=_("Blog"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ThreadMessage(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=50)
    website = models.URLField(_("Website"), max_length=50, null=True, blank=True)
    message = models.TextField(_("Message"), max_length=1000)
    thread = models.ForeignKey(Thread, verbose_name=_("Thread"), on_delete=models.CASCADE)
    parent = models.ForeignKey("self", verbose_name=_("Parent"), related_name="childs", on_delete=models.CASCADE, null=True, blank=True)

