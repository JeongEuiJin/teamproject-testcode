from django.contrib.auth import authenticate
from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from member.permissions import ObjectIsRequestUser
from .models import User
from .serializers import UserSerializer, UserCreationSerializer, UserLoginSerializer


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
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser,
    )
