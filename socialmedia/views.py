from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.admin import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from post.models import Post
from post.paginations import PostPagination
from post.serializers import PostRetrieveSerializer
from socialmedia.permissons import IsSelfOrReadOnly
from socialmedia.serializer import UserAvatarSerializer, UserSummarySerializer


class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model()
    permission_classes = [IsAuthenticated, IsSelfOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            from socialmedia.serializer import UserAdminAccessSerializer
            return UserAdminAccessSerializer
        else:
            from socialmedia.serializer import UserBaseAccessSerializer
            return UserBaseAccessSerializer


class UserAvatarAPIView(RetrieveUpdateAPIView):
    queryset = get_user_model()
    serializer_class = UserAvatarSerializer
    permission_classes = [IsAuthenticated, IsSelfOrReadOnly]


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    #filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'first_name', 'last_name']
    #
    # pagination_class = SearchResultsSetPagination

    serializer_class = UserSummarySerializer


class UserTimelineListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostRetrieveSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        return self.request.user.posts.all()


class PostListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PostPagination
    serializer_class = PostRetrieveSerializer

    def get_queryset(self):
        user = get_object_or_404(get_user_model(), id=self.kwargs['pk'])
        return user.posts.all()
