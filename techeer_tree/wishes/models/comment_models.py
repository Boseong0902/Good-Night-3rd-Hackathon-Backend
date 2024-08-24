from django.db import models
from .wish_models import Wish

class Comment(models.Model):
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content[:20] 