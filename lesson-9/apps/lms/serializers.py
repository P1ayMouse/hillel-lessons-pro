from rest_framework import serializers

from apps.lms.models import Student, Teacher, Group


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_date']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'birth_date']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'students_count']

    students_count = serializers.SerializerMethodField()

    def get_students_count(self, group):
        return group.students.count()
