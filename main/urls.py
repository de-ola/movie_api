from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name="category"),
    path('category/<str:name>/movies/', MovieListView.as_view(), name="movie_list"),
    path('category/<str:name>/movies/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('watch/movie/<int:id>/', MovieView.as_view(), name="watch_movie"),
]