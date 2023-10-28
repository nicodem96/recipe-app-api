from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView

app_name = 'dj_rest_auth.registration'

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    ]
