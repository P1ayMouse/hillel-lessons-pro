from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Student


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('lms:student-list')
    fields = ['name', 'birth_date']

    def get_form(self):
        form = super().get_form()
        form.fields['birth_date'].widget = DatePickerInput()
        return form


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('lms:student-list')
    fields = ['name', 'birth_date']

    def get_form(self):
        form = super().get_form()
        form.fields['birth_date'].widget = DatePickerInput()
        return form
