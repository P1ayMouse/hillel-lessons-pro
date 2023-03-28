from apps.authentication.serializer import UserSerializer, RegistrationUserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, CreateAPIView

User = get_user_model()


class CurrentUserDetailsView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserRegistrationView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegistrationUserSerializer
    queryset = User.objects.all()
