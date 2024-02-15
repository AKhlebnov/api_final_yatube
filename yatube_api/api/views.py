from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


from posts.models import Post, Group, Follow
from .serializers import (
    CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer)
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Класс представления для взаимодействия с постами."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Функция присвоения автора к объекту."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Класс представления для взаимодействия с комментариями к посту."""
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        """Функция присвоения автора и поста к объекту."""
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=int(post_id))

    def get_queryset(self):
        """Функция возвращения queryset(а) комментариев поста."""
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс представления для чтения групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny, ]


class FollowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """Класс представления для взаимодействия с подписчиками."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', )

    def get_queryset(self):
        """Функция возвращения queryset(а) подписок."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Функция присвоения автора к объекту."""
        serializer.save(user=self.request.user)
