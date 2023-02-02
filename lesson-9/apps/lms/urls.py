from django.urls import path

from apps.lms.views import hello, abc

app_name = 'lms'

urlpatterns = [
    path('', hello),
    path('abc/', abc),
]
