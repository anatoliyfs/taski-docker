"""Файл сериализаторов."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор модели Task."""

    class Meta:
        """Метаданные сериализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
