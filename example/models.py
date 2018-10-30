# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# from django_mysql_fields.fields.jsonfield import JSONField
from django.contrib.postgres.fields import JSONField

# Create your models here.


class one_model(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'模块名')

    def __unicode__(self):
        return self.name


class two_model(models.Model):
    model_name = models.ForeignKey(one_model)
    name = models.CharField(max_length=50, verbose_name=u'模块子项')

    def __unicode__(self):
        return self.name


class Example(models.Model):
    zixiang_name = models.ForeignKey(two_model)
    # 次测试详情， 预制条件，操作步骤，预期结果，实际结果， 错误等级，定性（优化，，，严重等）
    examples = JSONField()

    def __unicode__(self):
        return self.zixiang_name.name
