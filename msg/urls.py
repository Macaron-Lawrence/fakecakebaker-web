from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index),
    path("article/<str:name>",views.article)
]
