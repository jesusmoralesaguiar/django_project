from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
# from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.aggregates import StringAgg, ArrayAgg


def validate_evenDiscipline(value):
    length = len(value)
    while length >= 0:
        length -= 1
        if value[length].isupper():
            raise ValidationError(
                _('%(value)s contains uppercase'),
                params={'value': value},
            )
        if value.find("-") != -1:
            raise ValidationError(
                _('%(value)s contains -'),
                params={'value': value},
            )


class Discipline(models.Model):
    name = models.SlugField(max_length=150, unique=True,
                            validators=[validate_evenDiscipline])
    # caas = models.ForeignKey(
    #     'caas.CaaS',
    #     on_delete=models.CASCADE,
    #     verbose_name='CaaS')
    email = models.EmailField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    cross = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Discipline"
        ordering = ["name"]


def validate_even(value):
    length = len(value)
    while length >= 0:
        length -= 1
        if value[length].isupper():
            raise ValidationError(
                _('%(value)s contains uppercase'),
                params={'value': value},
            )

class ProductManager(models.Manager):
    def name_list(self):
        return self.aggregate(total_names = StringAgg("name", delimiter=', ', ordering="name"))

class Product(models.Model):
    from overlay.models import Overlay as OverlayModel
    objects = ProductManager()
    name = models.SlugField(
        unique=True,
        max_length=150,
        validators=[validate_even])
    type = models.CharField(max_length=1)
    description = models.CharField(max_length=150)
    overlay = models.ForeignKey(OverlayModel, on_delete=models.CASCADE,
                                verbose_name='Overlay/Product')
    base_file = models.CharField(max_length=150, verbose_name='base file')
    base_commit = models.SlugField(
        max_length=150,
        validators=[validate_even],
        blank=True,
        null=True)
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        verbose_name='Discipline')
    # network_file = models.ForeignKey(
    #     'Network_File',
    #     on_delete=models.CASCADE,
    #     verbose_name='Network File')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"
        ordering = ["name"]
