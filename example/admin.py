# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(one_model)
admin.site.register(two_model)
admin.site.register(Example)
