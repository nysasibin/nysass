from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet

router = DefaultRouter()
router.register(r'', UserLoginViewSet, basename='user-login'),


urlpatterns = [
    path('',include(router.urls)),
]
