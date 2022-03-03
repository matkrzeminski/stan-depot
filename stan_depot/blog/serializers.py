from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    formatted_content = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "hero",
            "content",
            "formatted_content",
            "status",
            "created",
            "modified",
            "publish",
        ]
