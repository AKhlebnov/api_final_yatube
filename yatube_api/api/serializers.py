from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, following_user):
        """
        Функция проверки уникальности подписки
        и недопустимости подписки на самого себя.
        """
        user = self.context['request'].user
        if user == following_user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        if Follow.objects.filter(user=user, following=following_user).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.'
            )

        return following_user
