# coding:utf-8
"""wechat URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from csd import views as csd_views
from common import views as common_views
import api

urlpatterns = [
    url(r'^wechat/admin/', include(admin.site.urls)),
    url(r'^wechat/$',csd_views.checkSignature),
    url(r'^wechat/get_access_token$',csd_views.getAccessToken),


    #测试用代码
    url(r'^wechat/getsessionlist/$',csd_views.get_session_list),
    url(r'^wechat/send_message$',csd_views.send_message),


]
