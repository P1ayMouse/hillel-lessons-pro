from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()


class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, related_name='groups', on_delete=models.PROTECT)
    students = models.ManyToManyField(Student, related_name='groups')
