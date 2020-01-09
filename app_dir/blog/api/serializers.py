from rest_framework import serializers

from app_dir.blog.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
        ]


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'slug',
            'category',
            'content'
        ]

