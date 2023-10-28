from django.urls import path, include
from .views import ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns =[
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path("registration/account-confirm-email/<key>", ConfirmEmailView.as_view(), name='account_confirm_email')
]
