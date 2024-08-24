from django.contrib import admin
from .models.wish_models import Wish
from .models.comment_models import Comment

admin.site.register(Wish)
admin.site.register(Comment)