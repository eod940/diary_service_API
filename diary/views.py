from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from diary.models import Post
from diary.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """
    게시글
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
