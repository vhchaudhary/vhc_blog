# -*- coding: utf-8 -*-

from django.conf.urls import  url
from .views import *


urlpatterns = [
    url(r'^newslatter/subscribe$', subscribe_newsletter,  name="subscribe_newsletter"),
]

