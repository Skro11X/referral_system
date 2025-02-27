import string
import random
from datetime import timedelta
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from referrals.models import ReferralCode


class CodeDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if ReferralCode.objects.filter(inviter=user).exists():
            return Response({"code": "already_have_invate_code"}, status=status.HTTP_400_BAD_REQUEST)
        length_of_code = 10
        chars = string.ascii_letters + string.digits
        code = ''.join(random.choices(chars, k=length_of_code))
        disabled_at = timezone.now().date() + timedelta(days=1)
        code_instance = ReferralCode.objects.create(inviter=user, code=code, disabled_at=disabled_at)
        send_mail(
            subject="Referral code",
            message=f"your referral code {code_instance.code}",
            from_email="testnoreplaytestnoreplay@gmail.com",
            recipient_list=[user.email,],
        )
        return Response({"status": "success", "message": "Письмо отправлено успешно."}, status=200)

    def delete(self, request):
        user = request.user
        code_instance = ReferralCode.objects.filter(inviter=user)
        if not code_instance.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        code_instance.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
