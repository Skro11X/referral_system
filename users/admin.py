from django.contrib import admin
from users.models import User
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
