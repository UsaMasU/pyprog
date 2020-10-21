from django.conf.urls import url
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),  # index view at /
    path('likepost/', views.likePost, name='likepost'),  # likepost view at /likepost
]
