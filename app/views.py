from django.shortcuts import render
# from requests import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .paginations import *
from .models import *
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class CreateView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = HomeSerializer
    # metadata_class = APIRootMetadata


    # def list(self, request, *args, **kwargs):
    #     return Response







    # filter_backends = [DjangoFilterBackend]
    # filterset_fields =["std"]
    #



    # for the paginations
    #
    # queryset = Student.objects.all()
    # serializer_class = HomeSerializer
    # pagination_class = Pagenations


    # for the ordering
    # queryset = Student.objects.all()
    # serializer_class = HomeSerializer
    # filter_backends = [OrderingFilter]
    # ordering_fields =['name']


    #for the seach

    # queryset = Student.objects.all()
    # serializer_class = HomeSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['std']

    #
    # serializer_class = HomeSerializer
    # def get_queryset(self):
    #
    #      return Student.objects.filter(std = 2)

