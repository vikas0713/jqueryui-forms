"""forms URL Configuration

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
from views import *
from rest_framework import serializers, viewsets, routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^$',index),
    url(r'^submit/',submit),
    url(r'^changed_status/(?P<lid>\d+)/$',changed_status),
    url(r'submit_info/(?P<status>\w+)/$', submit_info),
    url(r'get_status/(?P<status>\w+)/$', get_status),
    url(r'api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()