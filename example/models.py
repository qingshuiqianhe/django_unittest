# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# from django_mysql_fields.fields.jsonfield import JSONField
# from django.contrib.postgres.fields import JSONField
from jsonfield import JSONField


# Create your models here.


class one_model(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'模块名')

    class Meta:
        verbose_name = u'模块'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def getAllModel(self):
        return one_model.objects.all()

    def __unicode__(self):
        return self.name


class two_model(models.Model):
    model_name = models.ForeignKey(one_model)
    name = models.CharField(max_length=50, verbose_name=u'模块子项')

    class Meta:
        verbose_name = u'子项'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def getAllZiXiang(self, one_model):
        return two_model.objects.filter(model_name_id=one_model)

    def __unicode__(self):
        return self.name


class Example(models.Model):
    zixiang_name = models.ForeignKey(two_model)
    # 次测试详情， 预制条件，操作步骤，预期结果，实际结果， 错误等级，定性（优化，，，严重等）
    examples = JSONField(null=True, default={})

    class Meta:
        verbose_name = u'测试条例'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def getExamples(self, two_model):
        return Example.objects.filter(zixiang_name_id=two_model)

    def getListExamples(self, exam=[]):
        return Example.objects.filter(id in exam)

    def __unicode__(self):
        return self.zixiang_name.name + self.examples


class reportsIndex(models.Model):
    text_name = models.CharField(max_length=100, verbose_name=u"测试报告名称")
    createTime = models.DateTimeField(u"创建时间", default=timezone.now)
    createUser = models.CharField(u"创建人", max_length=50)

    class Meta:
        verbose_name = u'测试报告'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.text_name + self.createUser

    def getAllReports(self):
        return reportsIndex.objects.all()


class reports(models.Model):
    """错误等级定义或不是bug，但需要优化在此不做定义，放到json内了，后期总结主要依赖error字段"""
    error_level = (
        ("0", u"无"),
        ("1", u"一般"),
        ("2", u"严重"),
        ("3", u"致命")
    )

    reportName = models.ForeignKey(reportsIndex)
    lastChangeTIme = models.DateTimeField(u"最后修改时间", auto_now_add=True)
    lastChangeUser = models.CharField(u'修改人', max_length=50)
    model_name = models.CharField(max_length=50, verbose_name=u'模块名')
    zixiang_name = models.CharField(max_length=50, verbose_name=u'模块子项')
    text_contens = JSONField(default={})
    errorLevel = models.CharField(max_length=4, choices=error_level, default=0)

    class Meta:
        verbose_name = u'测试报告详情'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        # db_table = 'reports'
        # managed = True

    def getContext(self, reportName):
        return reports.objects.filter(reportName_id=reportName)
