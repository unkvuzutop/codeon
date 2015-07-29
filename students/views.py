#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.forms import EditStudentForm, CreateStudentForm
from students.models import Group, Student


class GroupListView(ListView):
    model = Group


class GroupCreate(CreateView):
    model = Group
    success_url = reverse_lazy('group_list')
    fields = ['title', 'steward']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GroupCreate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('student_list', args=(self.object.id,))


class GroupEdit(UpdateView):
    model = Group
    success_url = reverse_lazy('group_list')
    fields = ['title', 'steward']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GroupEdit, self).dispatch(request, *args, **kwargs)


class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('group_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GroupDelete, self).dispatch(request, *args, **kwargs)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        return Student.objects.filter(group_id=self.kwargs['pk'])


class StudentCreate(CreateView):
    model = Student
    form_class = CreateStudentForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StudentCreate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('student_list', args=(self.object.group.id,))


class StudentEdit(UpdateView):
    model = Student
    form_class = EditStudentForm
    success_url = reverse_lazy('student_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StudentEdit, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('student_list', args=(self.object.group.id,))


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StudentDelete, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('student_list', args=(self.object.group.id,))


def logout_view(request):
    logout(request)
