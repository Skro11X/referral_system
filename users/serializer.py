from djoser.serializers import UserCreateMixin, UserCreateSerializer
from rest_framework import serializers
from referrals.models import ReferralCode
from rest_framework.validators import UniqueValidator
from users.models import User


class CustomUserCreateSerializer(UserCreateMixin, serializers.Serializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    code = serializers.CharField(max_length=10, min_length=10, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        code = attrs.pop('code')
        code_instance = ReferralCode.objects.filter(code=code)
        if not code_instance.exists():
            return {**attrs, 'code': None}
        attrs['code'] = code_instance.first().inviter
        return attrs
