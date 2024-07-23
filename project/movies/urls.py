# movies/urls.py
from django.urls import path
from .views import  movie_detail

urlpatterns = [
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
]
