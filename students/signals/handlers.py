#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from students.models import Student, Group, EventHistory


@receiver(post_save, sender=Student)
@receiver(post_save, sender=Group)
@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def my_handler(sender, **kwargs):
    history = EventHistory(related_id=kwargs['instance'].id,
                           model=kwargs['instance']._meta.db_table)
    if 'created' not in kwargs:
        history.event = 'delete'
    elif 'created' in kwargs and kwargs['created'] is False:
        history.event = 'update'
    elif 'created' in kwargs and kwargs['created'] is True:
        history.event = 'insert'
    history.save()
