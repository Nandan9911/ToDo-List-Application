from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from .models import *

#CRUD OPERATIONS

class ListTodo(generics.ListAPIView): 
    permission_classes = (permissions.IsAuthenticated,)    # Read opeartion
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):   # Update opeartion
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView): 
    permission_classes = (permissions.IsAuthenticated,)  # Create opeartion
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):  # Delete opeartion
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


