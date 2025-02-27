from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    code = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
