from django.contrib import admin

# Register your models here.
from referrals import models

@admin.register(models.ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    pass

