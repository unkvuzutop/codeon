#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class ModelsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'test')
        self.test_row_id = 1

    def test_create_student_without_login(self):
        """
        Check access rights for Student creation
        """
        response = self.client.get(reverse('student_create'))
        self.assertEqual(response.status_code, 302, 'We can create '
                                                    'student without login')

    def test_create_group_without_login(self):
        """
        Check access rights for Group creation
        """
        response = self.client.get(reverse('group_create'))
        self.assertEqual(response.status_code, 302, 'We can create '
                                                    'group without login')

    def test_add_group_and_student(self):
        """
        1) Login
        2) Create Group and check result
        3) Create Student with created group_id and check result
        4) Get current Student list page and check count of objects
        on that page

        folder with test image /static/testimg.jpg
        """
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('group_create'),
                                    {'title': 'Test group'})
        self.assertRedirects(response,
                             '/studentlist/1',
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True,
                             msg_prefix='Can\'t add group')

        with open(os.getcwd()+'/static/testimg.jpg') as image:
            form_data = {'full_name' : 'Test Full Name',
                         'photo': image,
                         'group': self.test_row_id,
                         'birth_date': datetime.strftime(datetime.now(),
                                                         '%Y-%m-%d %H:%M:%S'),
                         'student_ticket_number': 2355}

            response = self.client.post(reverse('student_create'), form_data)

        self.assertRedirects(response,
                             '/studentlist/1',
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True,
                             msg_prefix='Can\'t add user')

        response = self.client.get(reverse('student_list',
                                           args=[self.test_row_id]))

        self.assertEqual(len(response.context['student_list']), 1)
