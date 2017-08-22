from django.conf.urls import url
from rest_framework.authtoken import views

from .. import apis

urlpatterns = [
    url(r'^postlist/$', apis.PostListAPIView.as_view(), name='post_postlist'),
    url(r'^create/$', apis.PostCreateAPIView.as_view(), name='post_create'),
    url(r'^(?P<pk>\d+)/$', apis.PostUpdateDestroyAPIView.as_view(), name='post_updatedestory'),
    url(r'^post_search/$', apis.PostListFindAPIView.as_view(), name='post_search'),
]
