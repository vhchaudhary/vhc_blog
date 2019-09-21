from django.core.exceptions import ValidationError
from django.db import models
from djangocms_video.models import ALLOWED_EXTENSIONS
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel


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


class Blog(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=100, blank=True, default='')
    title = models.CharField(_("Title"), max_length=100, blank=True, default='')
    url = models.URLField(_("URL"), blank=True, default='')
    image = FilerImageField(verbose_name=_("Image"), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    small_image = FilerImageField(verbose_name=_("Mobile Image"), null=True, related_name='+', blank=True, on_delete=models.SET_NULL)
    video_file = FilerFileField(verbose_name=_("Video file"), null=True, blank=True, related_name='+', on_delete=models.SET_NULL,
                                help_text=_('Allowed extensions: {extension}').format(extension=ALLOWED_EXTENSIONS))
    tech = models.ForeignKey(Technology, verbose_name=_("Technology"),  on_delete=models.SET_NULL, null=True)
    content = models.TextField(_('Content'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)

    def __str__(self):
        return self.name

    # def clean(self):
    #     if self.file and self.file.extension not in ALLOWED_EXTENSIONS:
    #         raise ValidationError(_('Incorrect file type: {extension}.').format(extension=self.file.extension))
