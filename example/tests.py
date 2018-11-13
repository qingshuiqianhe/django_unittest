# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


from .models import *
from django.test import TestCase
from django.test.utils import override_settings
# from django.db import connection


class TestModels(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        one_model.objects.create('test1')
        two_model.objects.bulk_create([
            two_model(name='test %s' % i, model_name='test1')
            for i in range(2, 10)
        ])

    @override_settings(DEBUG=True)
    def test_filter(self):
        two_models = two_model.objects.filter(model_name='test1').defer('name')
        # print connection.queries

