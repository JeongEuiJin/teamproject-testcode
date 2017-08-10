from django.contrib.auth import authenticate, get_user_model

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout as django_logout
from member.permissions import ObjectIsRequestUser
from django.utils.translation import ugettext_lazy as _

from .serializers import UserSerializer, UserCreationSerializer, UserLoginSerializer

User = get_user_model()


class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serial_data = UserLoginSerializer(request.data)
        plot_user = authenticate(email=serial_data.data["email"],
                                 password=serial_data.data["password"])
        if plot_user:
            token = Token.objects.get_or_create(user=plot_user)[0]
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "아이디 혹은 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response({"detail": _("토큰이 제공되지 않았습니다.")},
                            status=status.HTTP_401_UNAUTHORIZED)

        django_logout(request)

        return Response({"detail": _("로그아웃 되었습니다.")},
                        status=status.HTTP_200_OK)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserCreationSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        ObjectIsRequestUser,
    )
