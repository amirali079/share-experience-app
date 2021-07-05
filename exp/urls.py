
from dj_rest_auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from auth.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('socialmedia.api_urls')),
    path('api/auth/', include('auth.api_urls')),
    path('api/post/', include('post.api_urls')),

    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

    path('auth/google', GoogleLogin.as_view(), name='google_login'),
]
