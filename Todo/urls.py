"""Todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from workplan.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view()),
    url(r'^workplan/', Workplan.as_view()),
    #url(r'^calendar/', include('calendarium.urls')),
    # calendar views
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$',
        MonthView.as_view(),
        name='calendar_month'),

    url(r'^calendar/$',
        CalendariumRedirectView.as_view(),
        name='calendar_current_month'),
    url(r'^hday/', holiday),
]
