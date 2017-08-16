import requests
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout as django_logout
# from ..utilt.permissions import ObjectIsRequestUser
from django.utils.translation import ugettext_lazy as _

from utilt.permissions import ObjectIsRequestUser
from .serializers import UserSerializer, UserCreationSerializer, UserLoginSerializer

User = get_user_model()


class TokenUserInfoAPIView(APIView):
    def post(self, request):
        token_string = request.data.get('token')
        try:
            token = Token.objects.get(key=token_string)
        except Token.DoesNotExist:
            raise APIException('token invalid')
        user = token.user

        return Response(UserSerializer(user).data)


class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serial_data = UserLoginSerializer(request.data)
        plot_user = authenticate(email=serial_data.data["email"],
                                 password=serial_data.data["password"])
        print('plot: {}'.format(serial_data))
        if plot_user:
            token = Token.objects.get_or_create(user=plot_user)[0]
            pk = plot_user.id
            return Response({"pk": pk, "token": token.key}, status=status.HTTP_200_OK)
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


class UserSignUp(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserCreationSerializer


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


class UserDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk=None):
        return Response(UserSerializer(request.user).data)


class FacebookLoginAPIView(APIView):
    permission_classes = (AllowAny,)

    APP_ACCESS_TOKEN = '{}|{}'.format(
        settings.FACEBOOK_APP_ID,
        settings.FACEBOOK_SECRET_CODE,
    )

    def post(self, request):
        token = request.data.get('token')
        if not token:
            raise APIException('token require')

        self.debug_token(token)
        user_info = self.get_user_info(token=token)
        if User.objects.filter(username=user_info['id']).exists():
            user = User.objects.get(username=user_info['id'])
        else:
            user = User.objects.create_facebook_user(user_info)

        token, token_created = Token.objects.get_or_create(user=user)
        ret = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }
        return Response(ret)

    def debug_token(self, token):
        url_debug_token = 'https://graph.facebook.com/debug_token'
        url_debug_token_params = {
            'input_token': token,
            'access_token': self.APP_ACCESS_TOKEN
        }
        response = requests.get(url_debug_token, url_debug_token_params)
        result = response.json()
        if 'error' in result or 'error' in result['data']:
            raise APIException('token invalid')
        else:
            return result

    def get_user_info(self, token):
        url_user_info = 'https://graph.facebook.com/v2.9/me'
        url_user_info_params = {
            'access_token': token,
            'fields': ','.join([
                'id',
                'name',
                'email',
                'first_name',
                'last_name',
                'picture.type(large)',
                'gender',
            ])
        }
        response = requests.get(url_user_info, params=url_user_info_params)
        result = response.json()
        return result
