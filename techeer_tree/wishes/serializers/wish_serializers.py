from rest_framework import serializers
from ..models.wish_models import Wish

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['id', 'title', 'content', 'category', 'created_at', 'is_confirm']
        read_only_fields = ['created_at', 'is_confirm']