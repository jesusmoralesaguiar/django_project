from django.db import models
from physics.models import Discipline


class Overlay(models.Model):
    action = models.SlugField(
        unique=True,
        max_length=150)
    disable = models.BooleanField(default=False, help_text="Disable it, if you want hide action",
                                  verbose_name="enabled")
    enabled = models.BooleanField(default=True, verbose_name="enabled")
    file = models.CharField(max_length=150)
    repository = models.CharField(max_length=150)
    commit = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150)
    upstream = models.BooleanField(default=False,
                                   help_text="Check this to allow other disciplines to execute"
                                             " this overlay through the projectfile.")
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        verbose_name='Discipline', null=True)

    def __unicode__(self):
        return self.action

    def __str__(self):
        return str("{0}").format(self.action)

    class Meta:
        verbose_name_plural = "Overlay"
        ordering = ["action"]