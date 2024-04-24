from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView
from .models import *
from .serializers import *

class TodoListAPI(ListAPIView):
    queryset = TodoApp.objects.all().order_by('ended', '-created')
    serializer_class = TodoSerializer

class DetailApi(RetrieveAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer


class TodoCreateAPI(ListCreateAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateAPI(RetrieveUpdateAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer


class TodoDeleteAPI(RetrieveDestroyAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer
