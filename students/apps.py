#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = "Students"

    def ready(self):
        """
        initial custom signals handlers in application
        """
        import  students.signals.handlers
