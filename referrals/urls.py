from django.urls import path
from referrals.views import CodeDetailView


urlpatterns = [
    path("referral_code/", CodeDetailView.as_view(), name="referral_code"),
]