from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoListAPI.as_view()),
    path('create/', TodoCreateAPI.as_view()),
    path('detail/<int:pk>', DetailApi.as_view()),
    path('update/<int:pk>', TodoUpdateAPI.as_view()),
    path('delete/<int:pk>', TodoDeleteAPI.as_view()),
]