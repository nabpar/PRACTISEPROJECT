from django.shortcuts import render
from .models import Topic
from .serializer import TopicSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework import generics

# Create your views here.


#this is for TOPIC curd operation


class GetTopic(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class CreateTopic(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer  


class UpdateTopic(UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer 


class DeleteTopic(DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer           


