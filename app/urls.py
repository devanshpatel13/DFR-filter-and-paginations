from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .views import *
#
# from rest_framework import routers
#
router = routers.DefaultRouter()
router.register("create", CreateView , basename = "create")

urlpatterns = [

    path('', include(router.urls)),

    path('auth', include('rest_framework.urls', namespace='rest_framework'))

]
