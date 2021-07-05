
from dj_rest_auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from exp_auth.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('socialmedia.api_urls')),
    path('api/exp_auth/', include('exp_auth.api_urls')),
    path('api/post/', include('post.api_urls')),

    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

    path('exp_auth/google', GoogleLogin.as_view(), name='google_login'),
]
