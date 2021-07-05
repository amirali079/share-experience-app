from rest_framework import serializers
from post.models import Post, Comment
from socialmedia.serializer import UserSummarySerializer


class PostCreateSerializer(serializers.ModelSerializer):
    creator = UserSummarySerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'created_at', 'title', 'description', 'creator')
        read_only_fields = ('id',)


class PostRetrieveSerializer(serializers.ModelSerializer):
    creator = UserSummarySerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'created_at', 'title', 'description', 'creator')
        read_only_fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    creator = UserSummarySerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id', 'created_at', 'content', 'creator', 'title')
        read_only_fields = ('id', 'Post')

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        validated_data['post'] = self.context['post']
        return super(CommentSerializer, self).create(validated_data)
