from django.conf.urls import patterns, include, url
from django.contrib import admin
from bwf.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hciproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home$', home, name='home'),

    url(r'^signup$', SignupView.as_view()  ),
    url(r'^login$', 'django.contrib.auth.views.login' ),
    url(r'^logout$', 'django.contrib.auth.views.logout' ),

    url(r'^admin/', include(admin.site.urls)),
)
