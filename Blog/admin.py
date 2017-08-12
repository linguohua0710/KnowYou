# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Blog.models import App,Carousel

# Register your models here.
admin.site.register(App)
admin.site.register(Carousel)