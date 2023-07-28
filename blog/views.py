from rest_framework import viewsets, filters, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Blog, Category, Spotlight
from .serializers import BlogSerializer, CategorySerializer, SpotLightSerializer


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blogs']
    lookup_field = 'blogs'

    def retrieve(self, request, *args, **kwargs):
        # Custom retrieve method to fetch blog by blogname
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SpotLightViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Spotlight.objects.all()
    serializer_class = SpotLightSerializer


class BlogReadOnlyViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blogs']
    lookup_field = 'blogs'
    http_method_names = 'get'
