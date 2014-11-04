from django.conf.urls import url
from hxjh.views import search, index

urlpatterns = [
    url(r'search/$', search),
    url(r'index/$',index),
]