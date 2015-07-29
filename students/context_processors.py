#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings


def add_settings(request):
    """
    add  key:value params from application settings into template context
    """
    return {key: getattr(settings, key) for key in dir(settings)}


