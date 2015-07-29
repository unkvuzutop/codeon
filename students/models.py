#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from django.core.exceptions import ValidationError
from django.utils.six import python_2_unicode_compatible

from util import models


def name_validator(full_name):
        """
        Checks is whether the full name consist of 3 words
        example : Иванов Николай Николаевич
        """
        reg = re.compile(
            u'^[а-яА-яa-zA-Z]+[\s]+[а-яА-яa-zA-Z]+[\s]+[а-яА-яa-zA-Z]+')
        if not reg.match(full_name) :
            raise ValidationError(u'Name {0} must be like '
                                  u'"Иванов Николай Николаевич"'
                                  .format(full_name))


@python_2_unicode_compatible
class Student(models.Model):
    full_name = models.CharField(blank=True,
                                 null=False,
                                 max_length=100,
                                 validators=[name_validator])
    photo = models.ImageField(upload_to='media/images')
    birth_date = models.DateTimeField(null=False)
    student_ticket_number = models.IntegerField(blank=False,
                                                null=False,
                                                default=0,
                                                unique=True)
    group = models.ForeignKey('Group',
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name


@python_2_unicode_compatible
class Group(models.Model):
    title = models.CharField(blank=True,
                             null=False,
                             max_length=100)
    steward = models.ForeignKey(Student,
                                related_name='steward',
                                related_query_name='steward',
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class EventHistory(models.Model):
    model = models.CharField(max_length=20,
                             blank=True,
                             null=False)
    related_id = models.IntegerField()
    event = models.CharField(max_length=10,
                             blank=True,
                             null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
