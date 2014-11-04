# -*- coding: UTF-8 -*-

from django.conf.urls import url
from hxjh.views import *

urlpatterns = [
    url(r'search/$', search),
    url(r'index/$',index),
    url(r'contact/$', contact)
]