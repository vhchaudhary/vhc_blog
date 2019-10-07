# -*- coding: utf-8 -*-

from django.conf.urls import  url
from .views import *


urlpatterns = [
    url(r'^newslatter/subscrib4$', subscribe_newsletter,  name="subscribe_newsletter"),
]

