from django.urls import path
from . import views, api_views


urlpatterns = [
    path('', views.all_todos, name='all-todos'),
    path('create_todo/', views.create_todo, name='create-todo'),
    path('todo/<int:pk>/', views.todo_detail, name='todo-detail'),
    path('pdfs/<int:pk>/', views.pdf_view, name='pdf_view'),
    path('api/todos/', api_views.TodoListAPIView.as_view(), name='api-todo-list'),
]