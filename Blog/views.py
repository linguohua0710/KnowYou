# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from Blog.models import App,Carousel,Article,Video,Comments

def article(request):
    context = {}
    app_user = App.objects.filter(id=1)
    print app_user[0]
    context['blog'] = app_user[0].name
    context['domain'] = app_user[0].domain

    list = App.objects.all()
    for app in list:
        print app.name
    carousel_list = Carousel.objects.all()

    for carousel in carousel_list:
        # print carousel.content.split(",")
        carousel.content = carousel.content.split(",")
    context['list_carousel'] = carousel_list

    context['list_article'] = Article.objects.filter(id__lte=7)

    # context['list_video'] = Video.objects.filter(id__lte=3)

    context['list_comments'] = Comments.objects.filter(id__lte=6)

    context['list_advice'] = Article.objects.order_by("-read_times", "resp_times", "pride_times")[:10]
    return render_to_response("views/article.html", context)

# Create your views here.
def index(request):
    context = {}
    app_user = App.objects.filter(id=1)
    print app_user[0]
    context['blog'] = app_user[0].name

    list = App.objects.all()
    for app  in list:
        print app.name
    carousel_list = Carousel.objects.all()

    for carousel in carousel_list:
        # print carousel.content.split(",")
        carousel.content = carousel.content.split(",")
    context['list_carousel'] = carousel_list

    context['list_article'] = Article.objects.filter(id__lte=7)

    # context['list_video'] = Video.objects.filter(id__lte=3)

    context['list_comments'] = Comments.objects.filter(id__lte=6)

    context['list_advice'] = Article.objects.order_by("-read_times","resp_times","pride_times")[:10]

    return render_to_response("mainboard.html", context)