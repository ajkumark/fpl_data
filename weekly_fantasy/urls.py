from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weekly_fantasy.views.home', name='home'),
    url(r'', include('fantasyapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
