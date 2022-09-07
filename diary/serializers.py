from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from diary.models import Post


def validate_password(password):
    """
    게시물 생성시 비밀번호 검증을 위한 함수입니다.
    - 비밀번호는 6글자 이상, 숫자 1개 이상입니다.
        - 위 조건을 만족한다면 password를 반환합니다.
        - 이외에는 ValidationError를 띄웁니다.
    """
    if len(password) >= 6 and any(char.isdigit() for char in password):
        return password
    else:
        raise ValidationError("비밀번호는 6글자 이상이어야 하고 그 안에 숫자가 1개 이상 들어가야 합니다.")


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
            "password",
            "created_at",
            "updated_at",
            "title",
            "content",
        )

    def create(self, validated_data):
        """
        게시물을 생성합니다.
        비밀번호 검증 후 암호화합니다.
        """
        validate_password(validated_data['password'])  # 비밀번호 검증(6자이상, 숫자 1개+)
        validated_data['password'] = make_password(validated_data.get('password'))  # 비밀번호 암호화
        return super(PostSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """
        게시물을 수정합니다.
        """
        if check_password(validated_data.pop('password'), instance.password):
            return super().update(instance, validated_data)
        return ValidationError("비밀번호가 다릅니다.")
