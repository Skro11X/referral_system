from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from referrals.serializer import ReferralSerializer
from users.models import User


class CustomViewSet(UserViewSet):
    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated])
    def referrals(self, request, id=None):
        user = self.get_object()
        referrals = User.objects.filter(code=user)
        serializer = ReferralSerializer(referrals, many=True)
        return Response(serializer.data)
