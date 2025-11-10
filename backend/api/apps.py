"""Файл конфигурации приложения."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфигурация приложения."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
