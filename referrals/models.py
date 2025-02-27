import uuid
from datetime import timedelta

from django.db import models
from users.models import User
from django.db.models.functions import Now


class ReferralCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    disabled_at = models.DateField(default=Now() + timedelta(days=7))
    inviter = models.OneToOneField(User, on_delete=models.CASCADE)

