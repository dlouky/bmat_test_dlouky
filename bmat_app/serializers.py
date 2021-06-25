#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:57:43 2021

@author: fmd
"""
from rest_framework import serializers

from bmat_app.models import MusicalWork


class MusicalWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalWork
        fields = ("uid", "title", "contributors", "iswc")
