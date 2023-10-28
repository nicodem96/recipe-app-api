from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers
from allauth.account import app_settings as allauth_account_settings


class CustomLoginSerializer(RestAuthLoginSerializer):
    username = None


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED) # noqa
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }


class ConfirmEmailSerializer(serializers.Serializer):
    key = serializers.CharField(write_only=True)
