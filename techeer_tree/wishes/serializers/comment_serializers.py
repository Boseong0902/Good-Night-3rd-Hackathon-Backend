from rest_framework import serializers
from ..models.comment_models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'wish', 'content', 'created_at']
        read_only_fields = ['created_at', 'wish']