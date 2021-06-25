#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:34:46 2021

@author: fmd
"""
from django.urls import path

from .views import MusicalWorkDetail, MusicalWorkList

urlpatterns = [
    path("", MusicalWorkList.as_view()),
    path("search_iswc/", MusicalWorkDetail.as_view(), name="search_iswc"),
]
