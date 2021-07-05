from django.urls import path

from socialmedia.views import UserAPIView, UserAvatarAPIView, UserTimelineListAPIView, PostListAPIView, UserListAPIView

urlpatterns = [
    path('user/<int:pk>/', UserAPIView.as_view(), name='user_api'),

    path('user/avatar/<int:pk>/', UserAvatarAPIView.as_view(), name='avatar_api'),

    path('user/timeline/', UserTimelineListAPIView.as_view(), name='timeline_api'),
    path('user/<int:pk>/Posts/', PostListAPIView.as_view(), name='user_posts_api'),
    path('user/', UserListAPIView.as_view(), name='user_list_api'),


]
