from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.lms.models import Student, Teacher, Group
from apps.lms.serializers import StudentSerializer, TeacherSerializer, GroupSerializer


class StudentListCreateView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class TeacherListCreateView(ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeachersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class GroupListCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
