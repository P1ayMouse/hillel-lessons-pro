from random import choice
from time import sleep

from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .models import Student


class StudentListView(ListView, LoginRequiredMixin):
    paginate_by = 10
    model = Student

    def get(self, request, *args, **kwargs):
        messages.success(request, 'message_1')
        messages.error(request, choice(['AAAA', 'BBB', 'CCC']))
        return super().get(request, *args, **kwargs)


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('lms:student-list')
    fields = ['name', 'birth_date']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['birth_date'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        result = super().form_valid(form)
        cache.delete('students-list')
        return result


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('lms:student-list')
    fields = ['name', 'birth_date']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['birth_date'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        result = super().form_valid(form)
        cache.delete('students-list')
        return result


class LongRunningView(View):
    def get(self, request):

        value = cache.get('long-running')

        if not value:
            sleep(5)
            value = 'ok + ok + ok'
            cache.add('long-running', value)
        return HttpResponse(value)
