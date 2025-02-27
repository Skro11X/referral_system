from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import CustomViewSet

router = DefaultRouter()
router.register(r'users', CustomViewSet, basename='user')

urlpatterns = router.urls
