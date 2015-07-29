#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras import SelectDateWidget
from students.models import Student


class EditStudentForm(forms.ModelForm):
    class Meta(object):
        model = Student
        fields = ('full_name',
                  'photo',
                  'birth_date',
                  'student_ticket_number',
                  'group')

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = SelectDateWidget()


class CreateStudentForm(forms.ModelForm):
    class Meta(object):
        model = Student
        fields = ('full_name',
                  'photo',
                  'birth_date',
                  'student_ticket_number',
                  'group')

    def __init__(self, *args, **kwargs):
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = SelectDateWidget()
