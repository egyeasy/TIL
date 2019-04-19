from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Movie, Score
from .forms import ScoreForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/list.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    score_form = ScoreForm()
    context = {
        'movie': movie,
        'score_form': score_form
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_http_methods("POST")
def create_score(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ScoreForm(data=request.POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.movie = movie
        score.user = request.user
        score.save()
    return redirect('movies:detail', movie_pk)

@login_required
@require_http_methods("POST")
def delete_score(request, movie_pk, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    score.delete()
    return redirect('movies:detail', movie_pk)
    
    