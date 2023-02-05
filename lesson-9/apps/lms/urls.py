from django.urls import path
from apps.lms.views import StudentListView, StudentCreateView, StudentUpdateView

app_name = 'lms'

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('student/', StudentCreateView.as_view(), name='student-create'),
    path('student/<str:pk>/', StudentUpdateView.as_view(), name='student-update')
]
