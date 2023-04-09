from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.authentication.api_views import CurrentUserDetailsView, UserRegistrationView

app_name = 'authentication'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user-info/', CurrentUserDetailsView.as_view(), name='current-user'),
    path('user-registration/', UserRegistrationView.as_view(), name='registration-user'),
]
