# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Ksiazki

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^lista/', login_required(ListView.as_view(model=Ksiazki)),
        name='lista'),
    url(r'^dodaj/$', views.KsiazkiCreate.as_view(), name='dodaj'),
    url(r'^edytuj/(?P<pk>\d+)/', views.KsiazkiUpdate.as_view(), name='edytuj'),
    url(r'^usun/(?P<pk>\d+)/', views.KsiazkiDelete.as_view(), name='usun'),
]
