from datetime import timedelta

from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView, ListCreateAPIView, \
    RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from socialmedia.models import User
from .models import Post, Comment
from .paginations import PostPagination, CommentPagination
from .permissions import IsCreatorOrReadOnly
from .serializers import PostCreateSerializer,  PostRetrieveSerializer, CommentSerializer


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



