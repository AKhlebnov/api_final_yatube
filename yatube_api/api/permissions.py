from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользовательский класс разрешений,
    который разрешает только владельцу объекта
    редактировать его. Другой пользователь может только просматривать.
    """

    def has_object_permission(self, request, view, obj):
        """Функция определения прав на объект."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
