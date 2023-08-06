from rest_framework import viewsets, filters, permissions, status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import AllowOnlyOneIP

from .models import Blog, Category, Spotlight
from .serializers import BlogSerializer, CategorySerializer, BlogSerializerOne, BlogSerializerReadOnly

# class BlogViewSet(viewsets.ModelViewSet):
#     # permission_classes = [permissions.IsAuthenticated,AllowOnlyOneIP]
#     # authentication_classes = [JWTAuthentication]
#
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'blogs']
#     lookup_field = 'blogs'
#
#     def retrieve(self, request, *args, **kwargs):
#         # Custom retrieve method to fetch blog by blogname
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#

from rest_framework import viewsets, filters, permissions, status
from rest_framework.response import Response

from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer

from rest_framework import viewsets, filters, permissions, status
from rest_framework.response import Response
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer




class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blogs']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        category_name = self.kwargs.get('category_name')
        blogs = Blog.objects.filter(category__title=category_name)
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





class BlogReadOnlyViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerReadOnly
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blogs']
    lookup_field = 'slug'
    http_method_names = ['get']


################################# NEw addition

# class BlogViewSetOne(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializerOne
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'blogs']
#     lookup_field = 'blogs'
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class BlogViewSetOne(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerOne
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blogs']
    lookup_field = 'slug'

    @action(detail=False, methods=['GET'], url_path='categories/(?P<category_title>[\w-]+)')
    def get_blogs_by_category(self, request, category_title=None):
        category = get_object_or_404(Category, title=category_title)
        blogs = Blog.objects.filter(category=category)
        page = self.paginate_queryset(blogs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)

