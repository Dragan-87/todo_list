from rest_framework import viewsets
from .models import TodoItem
from .serializer import TodoSerializer

# Create your views here.

class TodoItemViewSet(viewsets.ModelViewSet):

    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
