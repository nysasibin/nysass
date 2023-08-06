# from django.urls import path, include
# from rest_framework import routers
# from .views import BlogViewSet, CategoryViewSet, SpotLightViewSet,BlogReadOnlyViewSet
#
# router = routers.DefaultRouter()
# router.register(r'blog',BlogViewSet)
# router.register(r'category',CategoryViewSet)
# router.register(r'spotlight',SpotLightViewSet)
# router.register(r'gsoftblogs',BlogReadOnlyViewSet)
#
#
#
# urlpatterns = [
#     path('',include(router.urls)),
#
# ]




from django.urls import path, include
from rest_framework import routers
from .views import BlogViewSet, CategoryViewSet, BlogViewSetOne, BlogReadOnlyViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'blogs', BlogReadOnlyViewSet)
router.register(r'categories', CategoryViewSet, basename='category')
#router.register(r'categories/(?P<category_name>[\w-]+)/blogs', BlogViewSetOne, basename='blogOne')
router.register(r'list', BlogViewSetOne, basename='blogOne')



urlpatterns = [
    path('', include(router.urls)),
]

