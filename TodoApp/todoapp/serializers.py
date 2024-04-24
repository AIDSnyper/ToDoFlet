from rest_framework.serializers import ModelSerializer
from .models import *


class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoApp
        fields = '__all__'
