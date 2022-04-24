from django.shortcuts import render
from .models import PRG
from .serializer import PRGSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import filters
from django.utils.text import slugify 
from .pagination import MyPagepagination
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework.parsers import FileUploadParser ,MultiPartParser,FormParser
# from taggit.models import Tag
# from .forms import BlogForm
# import requests
# Create your views here.

# class BlogCRUD(ModelViewSet):
#     queryset = BLOG.objects.all()
#     serializer_class = BlogSerializer

class GetAPI(ListAPIView):
    queryset = PRG.objects.all()
    serializer_class = PRGSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content'],
    pagination_class = MyPagepagination
    permission_classes = [IsAuthenticated] 
    # search_fields = ['^title','tags_title']
    # parser_classes = (FileUploadParser,MultiPartParser,FormParser)
    # common_tags = BLOG.tags.most_common()[:4]
    # form = BlogForm(BLOG)
    # if form.is_valid():
    #     newpost = form.save(commit=False)
    #     newpost.slug = slugify(newpost.title)

class CreateAPI(CreateAPIView):
    queryset = PRG.objects.all()
    serializer_class = PRGSerializer
    # parser_classes = (MultiPartParser,FormParser)


class UpdateAPI(generics.UpdateAPIView):
    queryset = PRG.objects.all()
    serializer_class = PRGSerializer
    permission_classes = [IsAdminUser]


class DeleteAPI(DestroyAPIView):
    queryset = PRG.objects.all()
    serializer_class = PRGSerializer       
