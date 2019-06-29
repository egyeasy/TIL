from django.shortcuts import render, redirect
from .models import Genre, Movie, Score


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    scores = movie.score_set.all()
    context = {
        'movie': movie,
        'scores': scores
    }
    return render(request, 'movies/detail.html', context)


def movie_edit(request, movie_id):
    context = {

    }
    return render(request, 'movies/edit.html', context)


def delete_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return redirect('movies:movie_list')


def create_score(request, movie_id):
    if request.method == 'POST':
        score = Score.objects.create(
            content=request.POST.get('content'),
            score=request.POST.get('score'),
            movie_id_id=movie_id,
        )
    return redirect('movies:movie_detail', movie_id)


def delete_score(request, movie_id, score_id):
    movie = Movie.objects.get(pk=movie_id)
    score = movie.score_set.get(pk=score_id)
    score.delete()
    return redirect('movies:movie_detail', movie_id)