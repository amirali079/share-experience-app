from django.shortcuts import render
from dj_rest_auth.registration.views import ConfirmEmailView
from django.shortcuts import reverse
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


def verified(request):
    return render(request, 'exp_auth/confirmEmail.html')


class CustomConfirmEmailView(ConfirmEmailView):
    def get_redirect_url(self):
        return reverse('account_email_verified')