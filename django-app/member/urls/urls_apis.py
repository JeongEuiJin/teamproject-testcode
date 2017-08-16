from django.conf.urls import url
from rest_framework.authtoken import views

from .. import apis

urlpatterns = [
    url(r'^userlist/$', apis.UserListCreateView.as_view(),name='member_userlist'),
    url(r'^signup/$', apis.UserSignUp.as_view(),name='member_signup'),
    url(r'^login/$',apis.UserLogin.as_view(),name='member_login'),
    url(r'^logout/$',apis.UserLogout.as_view(),name='member_logout'),
    url(r'^(?P<pk>\d+)/$', apis.UserRetrieveUpdateDestroyView.as_view(), name='member_detail'),
    url(r'^info/$', apis.UserDetailView.as_view()),
    url(r'^facebook-login/$', apis.FacebookLoginAPIView.as_view()),
    url(r'^token-user-info/$', apis.TokenUserInfoAPIView.as_view()),
    # url(r'^login1/$', views.ObtainAuthToken.as_view(), name='user-login'),
]
