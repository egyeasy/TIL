from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from movies.models import Score
from .forms import UserCustomCreationForm

# Create your views here.
def list(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/list.html', context)

def detail(request, user_pk):
    target_user = get_object_or_404(get_user_model(), pk=user_pk)
    target_email = target_user.email.encode(encoding='utf-8')
    print(target_email)
    context = {
        'target_user': target_user,
        'target_email': target_email,
    }
    if target_user == request.user:
        best_movies = []
        for following in target_user.followings.all():
            if following.score_set.all():
                the_movie = following.score_set.all().order_by('-value').first().movie
                best_movies.append([following, the_movie])
        # best_movie = Score.objects.filter(user__in=target_user.followings.all()).order_by('value').first().movie
        context['best_movies'] = best_movies
    return render(request, 'accounts/detail.html', context)

@login_required
def follow(request, user_pk):
    target_user = get_object_or_404(get_user_model(), pk=user_pk)
    # if request.user in target_user.followers.all():
    if target_user in request.user.followings.all():
        target_user.followers.remove(request.user)
    else:
        target_user.followers.add(request.user)
    return redirect('accounts:detail', user_pk)


def followers(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'follows': user.followers.all()
    }
    return render(request, 'accounts/follows.html', context)


def followings(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'follows': user.followings.all()
    }
    return render(request, 'accounts/follows.html', context)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')