#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from .models import Student, Group, EventHistory


class StudentInline(AdminImageMixin, admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'steward')
    inlines = [
        StudentInline,
    ]

admin.site.register(Group, GroupAdmin)


class StudentAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'photo_thumbnail', 'group')

    def photo_thumbnail(self, obj):
        image = get_thumbnail(obj.photo, '60x60', quality=99)
        return format_html(
            '<img src="{}" border="0" alt="" width="{}" height="{}" />',
            image.url, image.width, image.height)

admin.site.register(Student, StudentAdmin)


class EventHistoryAdmin(admin.ModelAdmin):
    list_display = ('model', 'event', 'date')

admin.site.register(EventHistory, EventHistoryAdmin)
