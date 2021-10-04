from django.urls import path
from .views import get_movies, get_movie

urlpatterns = [
    path('', get_movies, name='get_movies'),
    path('<int:pk>', get_movie, name='get_movies'),
]
