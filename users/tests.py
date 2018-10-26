# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import users


class UsersTestCase(TestCase):

    def setUp(self):
        users.objects.create(name='ss1', address='ss11')
        users.objects.create(name='ssx2', address='ss11x')
        auths = users.objects.all()
        print auths

    def tearDown(self):
        users.objects.filter(name='ss').delete()
        auths = users.objects.all()
        print auths

    def test_insert_user(self):
        users.objects.create(name='ss3', address='ss1')
        users.objects.create(name='ssx', address='ss1x')
        auths = users.objects.all()
        print auths

    def test_update_user(self):
        users.objects.create(name='ssx', address='ss1x')
        auth = users.objects.get(name='ssx')
        auth.address = 'ssssdfasdf'
        auth.email = '111@xx.com'
        auth.save()
        print auth.address, auth.name, auth.email
        auths = users.objects.all()
        print auths


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

if __name__ == '__main__':
    auths = UsersTestCase()
    auths.setUp()
    auths.test_insert_user()
    auths.test_update_user()
    auths.tearDown()
