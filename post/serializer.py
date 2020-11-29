from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    text = serializers.CharField()
    author_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
