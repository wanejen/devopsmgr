from django.conf.urls import include, url
from django.contrib import admin
from hxjh import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'devopsmgr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hxjh/name/', 'hxjh.views.hxjh_test'),
]
