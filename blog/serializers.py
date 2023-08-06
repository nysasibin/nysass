from rest_framework import serializers

from .models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Blog
        fields = ['id', 'slug', 'title', 'read_time', 'category', 'image1', 'body1', 'image2', 'body2', 'image3','body3','image4', 'body4', 'created', 'modified', 'post', 'post_published']
        extra_kwargs = {
            'image2': {'required': False},
            'image3': {'required': False},
            'image4': {'required': False},
            'body2': {'required': False},
            'body3': {'required': False},
            'body4': {'required': False},
            'category': {'required': False},

        }


############################## New For catagory


# class BlogSerializerOne(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#
#     class Meta:
#         model = Blog
#         fields = ['id', 'blogs', 'title', 'read_time', 'category', 'image1', 'body1', 'post', 'post_published']


class BlogSerializerOne(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Blog
        fields = ['id', 'slug', 'title', 'category', 'image1', 'body1', 'post']



class BlogSerializerReadOnly(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Blog
        fields = ['id', 'slug', 'title', 'read_time', 'category', 'image1', 'body1', 'image2', 'body2', 'image3','body3','image4', 'body4', 'created', 'modified', 'post', 'post_published']
        extra_kwargs = {
            'image2': {'required': False},
            'image3': {'required': False},
            'image4': {'required': False},
            'body2': {'required': False},
            'body3': {'required': False},
            'body4': {'required': False},
            'category': {'required': False},

        }


