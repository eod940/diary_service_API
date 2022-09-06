from django.db import models


class TimeStampedModel(models.Model):
    """
    created_at, updated_at 필드 생성을 위한 기본 모델
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일자")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일자")

    class Meta:
        abstract = True


class CommonPostModel(models.Model, TimeStampedModel):
    """
    모든 게시물이 공유하는 필드 생성을 위한 기본 모델
    """
    title = models.CharField(max_length=20, verbose_name="제목")
    content = models.CharField(max_length=200, verbose_name="내용")
    password = models.CharField(max_length=128, verbose_name="비밀번호")

    class Meta:
        abstract = True


class Post(CommonPostModel):
    """
    사용자가 생성하는 게시물입니다.
    최신순으로 정렬합니다.
    """
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{}'.format(self.title)
