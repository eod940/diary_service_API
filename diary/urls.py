from django.urls import path, include
from rest_framework.routers import DefaultRouter

from diary.views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)  # 게시글

urlpatterns = [
    path('', include(router.urls))
]