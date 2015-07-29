#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from students.models import Group, Student


class ModelsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'test')

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
        2) Create Group
        3) Check group present in DB
        4) Check redirect after creation of the group
        3) Create Student with created group_id
        4) Check student present in DB
        5) Check redirect after creation of the  student
        4) Get current Student list page and check count of objects
        on that page

        folder with test image /static/testimg.jpg
        """
        self.client.login(username='test', password='test')
        group_data = {'title': 'Test group'}
        response = self.client.post(reverse('group_create'),
                                    group_data)
        get_latest_group = Group.objects.latest('id')

        self.assertEqual(get_latest_group.title, group_data['title'])
        self.assertRedirects(response,
                             '/studentlist/' + str(get_latest_group.id),
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True,
                             msg_prefix='Can\'t add group')

        with open(os.getcwd() + '/static/testimg.jpg') as image:
            form_data = {'full_name': 'Test Full Name',
                         'photo': image,
                         'group': str(get_latest_group.id),
                         'birth_date': datetime.strftime(datetime.now(),
                                                         '%Y-%m-%d %H:%M:%S'),
                         'student_ticket_number': 2355}

            response = self.client.post(reverse('student_create'), form_data)

        get_latest_student = Student.objects.latest('id')
        self.assertEqual(get_latest_student.full_name, form_data['full_name'])
        self.assertRedirects(response,
                             '/studentlist/' + str(get_latest_group.id),
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True,
                             msg_prefix='Can\'t add user')
        response = self.client.get(reverse('student_list',
                                           args=[get_latest_group.id]))
        self.assertEqual(len(response.context['student_list']), 1)
