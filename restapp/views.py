import django_filters.rest_framework
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Task
from .serializers import TaskSerializers, UserSerializier


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filter_fields = ('completed', )
    ordering = ('-date_created', )
    search_fields = ('task_name', 'task_description')


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializier


"""
class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(
        completed=False)
    serializer_class = TaskSerializers


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(
        completed=True)
    serializer_class = TaskSerializers
"""
