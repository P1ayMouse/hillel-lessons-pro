from django.urls import path

from apps.lms.api_views import StudentListCreateView, StudentsRetrieveUpdateDestroyView, \
    TeacherListCreateView, TeachersRetrieveUpdateDestroyView, \
    GroupListCreateView, GroupsRetrieveUpdateDestroyView

app_name = 'api-lms'

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('students/<str:pk>/', StudentsRetrieveUpdateDestroyView.as_view()),
    path('teachers/', TeacherListCreateView.as_view()),
    path('teachers/<str:pk>/', TeachersRetrieveUpdateDestroyView.as_view()),
    path('groups/', GroupListCreateView.as_view()),
    path('groups/<str:pk>/', GroupsRetrieveUpdateDestroyView.as_view()),
]
