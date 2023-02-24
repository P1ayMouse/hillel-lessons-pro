from django.urls import path

from apps.authentication.views import (AccountView, LoginView, LogoutView, RegisterView, UserConfirmView)

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/<str:token>/', UserConfirmView.as_view(), name='confirm'),
]
