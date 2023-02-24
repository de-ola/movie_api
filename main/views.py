from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics, pagination, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]

class MovieListView(APIView):
    def get(self, request, format=None, **kwargs):
        movie = Movie.objects.filter(category__name = kwargs["name"])
        serializer = MovieListSerializer(instance=movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieDetailView(APIView):
    def get(self, request, format=None, **kwargs):
        movie = Movie.objects.filter(category__name = kwargs["name"]).filter(id=kwargs["pk"]).first()
        serializer = MovieDetailSerializer(instance=movie)
        return Response(serializer.data)

class MovieView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'