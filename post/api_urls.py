from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
    path('<int:pk>/', PostRetrieveDestroyAPIView.as_view(), name='post_retrieve_destroy'),
    path('', PostCreateAPIView.as_view(), name='post_create'),

    path('<int:post_pk>/comment/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
    path('<int:post_pk>/comment/<int:comment_pk>/', CommentRetrieveDestroyAPIView.as_view(), name='comment_retrieve_destroy'),

]

