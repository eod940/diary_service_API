from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from diary.models import Post


class PostSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='비밀번호는 6자 이상, 숫자 1개 이상이어야 합니다.',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "password",
            "created_at",
            "updated_at",
            "title",
            "content",
        )

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(PostSerializer, self).create(validated_data)


