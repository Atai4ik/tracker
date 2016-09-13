#coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class DetailProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь', related_name='prof')
    avatar = models.ImageField(u'Фотография пользователя', upload_to='upload/avatar_pic/', blank=True, null=True)
    first_name = models.CharField(u'Имя', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    slug = models.SlugField(unique=True)
    birthday = models.DateField(u'Дата рождения', blank=True, null=True)
    phone = models.CharField(u'Телефон', max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=None)

    class Meta:
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'

    def __unicode__(self):
        return self.first_name
