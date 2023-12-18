# learning_platform/learning_app/learning_app/api_urls.py

from django.urls import path
from . import api_views

urlpatterns = [
    path('todos/', api_views.TodoListAPIView.as_view(), name='api-todo-list'),
]
