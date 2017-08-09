from django.conf.urls import url
from rest_framework.authtoken import views

from .. import apis

urlpatterns = [
    url(r'^$', apis.UserListCreateView.as_view(),name='member_list'),
    # url(r'^login1/$',apis.UserLogin.as_view(),name='member_login'),
    url(r'^(?P<pk>\d+)/$', apis.UserRetrieveUpdateDestroyView.as_view(), name='member_detail'),
    url(r'^login/$', views.ObtainAuthToken.as_view(), name='user-token'),
]
