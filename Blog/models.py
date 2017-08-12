# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class App(models.Model):
    id = models.IntegerField(primary_key=True)
    gmt_create = models.BigIntegerField()
    gmt_modified = models.BigIntegerField()
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Carousel(models.Model):
    id = models.IntegerField(primary_key=True)
    gmt_create = models.BigIntegerField()
    gmt_modified = models.BigIntegerField()
    index = models.IntegerField()
    img = models.CharField(max_length=128)
    content = models.TextField()

    def __unicode__(self):
        return self.content

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    gmt_create = models.BigIntegerField()
    gmt_modified = models.BigIntegerField()
    category = models.CharField(max_length=32)
    publish_time = models.BigIntegerField()
    img = models.CharField(max_length=128)
    title = models.CharField(max_length=512)
    content = models.TextField()
    resp_times = models.IntegerField()
    read_times = models.IntegerField()
    pride_times = models.IntegerField()

class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    gmt_create = models.BigIntegerField()
    gmt_modified = models.BigIntegerField()
    type = models.CharField(max_length=32)
    video = models.CharField(max_length=128)
    content = models.TextField()

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    gmt_create = models.BigIntegerField()
    gmt_modified = models.BigIntegerField()
    title = models.CharField(max_length=128)
    comment = models.CharField(max_length=256)