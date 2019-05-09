from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Score
from .serializer import GenreSerializer, MovieSerializer, ScoreSerializer

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    fields = ('id', 'name')
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, fields=fields, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    serializer = GenreSerializer(genre)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_update_delete_score(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        request.data["movie"] = score.movie_id
        serializer = ScoreSerializer(instance=score, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        score.delete()
        return Response({'message': '삭제되었습니다.'})
    


@api_view(['POST'])
def create_score(request, movie_id):
    # movie = get_object_or_404(Movie, pk=movie_id)
    request.data["movie"] = movie_id
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message': '작성되었습니다.'})