# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import *

"""首页的一级模块展示， 点击一级模块后展示对应的模块子项，同理点击后展示具体的测试条例"""


def index(request):
    one_models = one_model()
    context = {"one_models": one_models.getAllModel()}
    return render(request, 'index.html', context)


def getZixiang(request, one_model):
    if one_model:
        two_models = two_model()
        try:
            context = {"zixiangs": two_models.getAllZiXiang(one_model)}
            print context
        except ValueError as e:
            context = {"msg": u"one_model index out range"}
        return render(request, 'index.html', context)
    context = {"msg": u"no index of one_model"}
    return render(request, 'index.html', context)


def getTiaoli(request, two_model):
    if two_model:
        examples = Example()
        try:
            context = {'examples': examples.getExamples(two_model)}
        except ValueError as e:
            context = {"msg": u"two_model index out range"}
        return render(request, 'index.html', context)
    context = {"msg": u"no index of two_model"}
    return render(request, 'index.html', context)


def createResports(request):
    """前端做好限制，勾选了上级自动勾选所有下级，否则视为单一勾选下级或者下下级"""
    if request.method == 'POST':
        try:
            text_name = request.POST.get('text_name', u'new test')
            exampleLists = request.POST.get('examples', [])
        except ValueError as e:
            print e
        reportsIndex.objects.create(text_name=text_name, createUser=request.user)
        exams = Example()
        examsQuerset = exams.getListExamples(exampleLists)
        for exam in examsQuerset:
            reports.objects.create(model_name=exam.zixiang_name.model_name, zixiang_name=exam.zixiang_name,
                                   text_contens=exam.examples)
        return render(request, 'index.html')
