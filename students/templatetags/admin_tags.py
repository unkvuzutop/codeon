#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from django import template

register = template.Library()


@register.simple_tag
def admin_url(instance):
    try:
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return '<a href="'\
               +urlresolvers.reverse("admin:%s_%s_change" %
                                                (content_type.app_label,
                                                 content_type.model),
                                                args=(instance.id,))\
               + '"><span class="glyphicon glyphicon-pencil" ' \
                 'aria-hidden="true"></span></a>'
    except:
        return ""
