from django.shortcuts import render, redirect
from .models import Genre, Movie, Score
from .forms import MovieModelForm, ScoreModelForm
from django.contrib import messages


# Create your views here.
# project 7 - database
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
    print(scores)
    return render(request, 'movies/detail.html', context)


def delete_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return redirect('movies:movie_list')



# project 8 - seed
def create_score(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        score = Score(movie_id=movie)
        form = ScoreModelForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, "댓글 형식을 잘못 입력하셨습니다")
    return redirect('movies:movie_detail', movie_id)


def delete_score(request, movie_id, score_id):
    movie = Movie.objects.get(pk=movie_id)
    score = movie.score_set.get(pk=score_id)
    score.delete()
    return redirect('movies:movie_detail', movie_id)


def movie_new(request):
    if request.method == "POST":
        form = MovieModelForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('movies:movie_detail', data.id)
        else:
            messages.success(request, "영화 정보를 잘못 입력하셨습니다")
            context = {
                'form': form,
            }
            return render(request, 'movies/form.html', context)
        # title = request.POST.get('title')
        # audience = request.POST.get('audience')
        # poster_url = request.POST.get('poster_url')
        # description = request.POST.get('description')
        # genre_id_id = request.POST.get('genre_id_id')
        # # genre_name = request.POST.get('genre_name')
        # # genre_id = Genre.objects.get(name=genre_name)

        # movie = Movie.objects.create(title=title,
        #                      audience=audience,
        #                      poster_url=poster_url,
        #                      description=description,
        #                      genre_id_id=genre_id_id)
    else:
        form = MovieModelForm()
        context = {
            'form': form
        }
        return render(request, 'movies/form.html', context)


def edit_movie(request, movie_id):
    # 영화 수정 form
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'GET':
        form =MovieModelForm(instance=movie)
        context = {
            'form': form
        }
        return render(request, 'movies/form.html', context)

    # 영화 수정 처리
    else:
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            data = form.save()
            return redirect('movies:movie_detail', data.id)
        else:
            messages.success(request, "영화 정보를 잘못 입력하셨습니다")
            return render('movies/form.html')
