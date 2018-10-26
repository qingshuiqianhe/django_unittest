# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class users(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=200, verbose_name='地址')

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.name



