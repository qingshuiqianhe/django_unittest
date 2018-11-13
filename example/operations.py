# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

"""对于建好的测试报告的操作，对某些条例的操作，批量的复制，删除。测试报告内容的修改"""
"""ajax 提交的数据后台可以创建对应新增的测试条例，在重新把所有条例返回前端渲染？？
还是后台创建，前端js增加td增显示时不标注example_id,，后台保存的时候在根据没有id去创建条例保存内容？？"""

def addExamples(request):
    try:
        exampleids = request.POST.get('example_id', [])
    except ValueError as e:
        pass


def delExamples(request):
    try:
        exampleids = request.POST.get('example_id', [])
    except ValueError as e:
        pass


def saveExamples(request):
    try:
        exampleids = request.POST.get('example_id', [])
    except ValueError as e:
        pass
