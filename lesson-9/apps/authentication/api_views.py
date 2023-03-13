from apps.authentication.serializer import UserSerializer
from rest_framework.generics import RetrieveAPIView


class CurrentUserDetailsView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
