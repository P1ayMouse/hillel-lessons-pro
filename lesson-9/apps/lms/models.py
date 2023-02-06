from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.


class Student(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    birth_date = models.DateField(_('Birth Date'))


class Teacher(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    birth_date = models.DateField(_('Birth Date'))


class Group(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    teacher = models.ForeignKey(Teacher, related_name='groups', on_delete=models.PROTECT)
    students = models.ManyToManyField(Student, related_name='groups')
