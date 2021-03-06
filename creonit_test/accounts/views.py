from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from .serializers import UserSerializer, RegisterSerializer


class RegisterAPI(generics.GenericAPIView):
    """
    Управление регистрацией пользователя с присвоением токена
    """

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Регистрация нового пользователя
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                'token': AuthToken.objects.create(user)[1]
            }
        )


class LoginAPI(KnoxLoginView):
    """
    Управление авторизацией пользователя по токену
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """
        Авторизация пользователя
        """

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
