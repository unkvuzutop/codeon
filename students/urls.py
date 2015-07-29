#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.static import static
from django.conf.urls import url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from students.views import GroupListView, GroupCreate, GroupEdit, GroupDelete,\
    StudentListView, StudentCreate, StudentEdit, StudentDelete

urlpatterns = [
    url(r'^$', GroupListView.as_view(), name='group_list'),
    url(r'^group/create$', GroupCreate.as_view(), name='group_create'),
    url(r'^group/edit/(?P<pk>\d+)$', GroupEdit.as_view(), name='group_edit'),
    url(r'^group/delete/(?P<pk>\d+)$', GroupDelete.as_view(),
        name='group_delete'),
    url(r'^studentlist/(?P<pk>\d+)$', StudentListView.as_view(),
        name='student_list'),
    url(r'^studentlist/create$', StudentCreate.as_view(),
        name='student_create'),
    url(r'^studentlist/edit/(?P<pk>\d+)$', StudentEdit.as_view(),
        name='student_edit'),
    url(r'^studentlist/delete/(?P<pk>\d+)$', StudentDelete.as_view(),
        name='student_delete'),
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            ) + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
