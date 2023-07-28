from django.urls import path, include
from rest_framework import routers
from .views import BlogViewSet, CategoryViewSet, SpotLightViewSet,BlogReadOnlyViewSet

router = routers.DefaultRouter()
router.register(r'blog',BlogViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'spotlight',SpotLightViewSet)
router.register(r'gsoftblogs',BlogReadOnlyViewSet)


urlpatterns = [
    path('',include(router.urls)),

]
