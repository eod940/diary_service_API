from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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

    def destroy(self, request, *args, **kwargs):
        """
        비밀번호 확인 후 맞다면 삭제
        비밀번호가 다르면 Error
        포스트가 없으면 404
        """
        try:
            password = request.data.get("password", None)
            instance_password = Post.objects.get(id=self.kwargs.get("pk"))

            if check_password(password, instance_password):
                return super(PostViewSet, self).destroy(request, *args, **kwargs)

            raise ValidationError("비밀번호를 확인해 주세요.")

        except Post.DoesNotExist as e:
            return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)