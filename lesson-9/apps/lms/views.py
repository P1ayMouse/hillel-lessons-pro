from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .models import Student


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('lms:student-list')
    fields = ['name', 'birth_date']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['birth_date'].widget = DatePickerInput()
        return form


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('lms:student-list')
    fields = ['name', 'birth_date']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['birth_date'].widget = DatePickerInput()
        return form
