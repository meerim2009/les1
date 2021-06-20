from django.contrib import admin
from django.urls import path

from test_app import views

urlpatterns = [
    path('posts/', views.get_posts),
    path('posts/<int:id>/', views.get_post),
    path('posts/<int:id>/comments/', views.get_comment),
]