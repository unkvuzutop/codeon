#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import AppCommand
from students.models import Group


class Command(AppCommand):
    help = 'Prints groups list with their students.'

    requires_system_checks = True

    def handle_app_config(self, app, **options):
        data = []
        for group in Group.objects.all():
            data.append('Group: ' + group.title)
            data.append('Student list:')
            for student in group.student_set.all():
                data.append(' '*10 + student.full_name)
        return '\n'.join(data)
