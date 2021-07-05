from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.authtoken.admin import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, ListAPIView, \
    RetrieveDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from post.models import Post, Comment
from post.paginations import PostPagination, CommentPagination
from post.permissions import IsCreatorOrReadOnly
from post.serializers import PostRetrieveSerializer, PostCreateSerializer, CommentSerializer


class PostRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]


class PostCreateAPIView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]
    lookup_url_kwarg = "comment_pk"

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return post.comments


class CommentListCreateAPIView(ListCreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super(CommentListCreateAPIView, self).get_serializer_context()
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return context

    def get_queryset(self):
            post = get_object_or_404(Post, id=self.kwargs['post_pk'])
            return post.comments.all()



