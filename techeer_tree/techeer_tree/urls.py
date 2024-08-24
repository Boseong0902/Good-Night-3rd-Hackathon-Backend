"""
URL configuration for techeer_tree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wishes.views.wish_views import *
from wishes.views.comment_views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishes/create/', WishCreateView.as_view(), name = 'ish-create'),
    path('wishes.delete/<int:pk>/',  WishDeleteView.as_view(), name = 'wish-delete'),
    path('wishes/confirm/<int:pk>/', WishConfirmView.as_view(), name='wish-confirm'),
    path('wishes/<int:pk>/', WishDetailView.as_view(), name='wish-detail'),
    path('wishes/', WishListView.as_view(), name='wish-list'),
    path('wishes/<int:wish_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('wishes/<int:wish_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]
