# learning_platform/learning_app/learning_app/api_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import todo
from .serializers import TodoSerializer


class TodoListAPIView(APIView):
    def get(self, request):
        todos = todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
