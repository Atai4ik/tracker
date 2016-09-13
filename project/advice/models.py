#coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Advice(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Совет')
        verbose_name_plural = _('Советы')

    def __unicode__(self):
        return self.title