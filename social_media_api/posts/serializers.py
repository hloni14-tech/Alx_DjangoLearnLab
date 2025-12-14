from rest_framework import serializers
from .models import Posts, Comments

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = [ 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['post', 'author', 'content', 'created_at', 'updated_at']
