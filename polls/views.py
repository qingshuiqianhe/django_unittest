# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.urls import reverse


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def index(request):
#         latest_question_list = Question.objects.order_by('-pub_date')[:5]
#         output = ','.join([q.question_text for q in latest_question_list])
#         return HttpResponse(output)
#
#     def get_queryset(self):
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print latest_question_list
    output = [q.queestion_tets for q in latest_question_list]
    # return HttpResponse({'output': output})
    return render(request, 'polls/index.html', {'output': output})
    # return HttpResponse(' looking at question %s.' % question_id)


def detail(request, question_id):
    return HttpResponse(' looking at question %s.' % question_id)


def results(request, question_id):
    response = 'looking at question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)

# def fob(n):
#     count = 0
#     a, b = 0, 1
#     while count < n:
#         res = a
#         a, b = b, a+b
#         count += 1
#         yield res
#
#
# fob = fob(10)
# for x in fob:
#     print x
#

def all(request):
    ques = Question.objects.all()
    content = {'ques': ques}
    return render(request, 'polls/index.html', context=content)
