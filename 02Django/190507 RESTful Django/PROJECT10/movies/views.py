from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Score
from .serializer import GenreSerializer, MovieSerializer, ScoreSerializer

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    serializer = GenreSerializer(genre)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def score_detail(request, score_id):
    score = Score.objects.get(pk=score_id)
    serializer = ScoreSerializer(score)
    return Response(data=serializer.data)