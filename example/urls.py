# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *
urlpatterns = [
    url(r'^getZixiang/(?P<one_model>[0-9]+)/$', getZixiang, name='getZixiang'),
    url(r'^getTiaoli/(?P<two_model>[0-9]+)/$', getTiaoli, name='getTiaoli'),

]
