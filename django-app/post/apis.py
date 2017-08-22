from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from post.serializers import PostSerializer, PostCreateSerializer
from utilt.permissions import ObjectIsRequestUser
from .models import Post


class PostListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        ObjectIsRequestUser,
    )
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer


class PostUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()


class PostListFindAPIView1(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('poster_title', 'poster_description', 'location', 'place')


class PostListFindAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        search_title = self.request.query_params.get('q')
        # search_title = self.request.poster_title
        post_search = Post.objects.filter(poster_title__contains=search_title)

        return post_search
