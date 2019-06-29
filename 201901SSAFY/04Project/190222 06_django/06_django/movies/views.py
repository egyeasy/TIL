from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def home(request):
    
    return redirect('movies:index')


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    
    return render(request, 'index.html', context)
    
    
def detail(request, movies_id):
    movie = Movie.objects.get(pk=movies_id)
    context = {
        'movie': movie
    }
    
    return render(request, 'detail.html', context)
    
def edit(request, movies_id):
    movie = Movie.objects.get(pk=movies_id)
    context = {
        'movie': movie
    }
    
    return render(request, 'edit.html', context)
    
def delete(request, movies_id):
    movie = Movie.objects.get(pk=movies_id)
    movie.delete()
    
    return redirect('movies:index')