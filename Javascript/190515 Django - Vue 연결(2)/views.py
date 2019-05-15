from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login # 함수명과 겹치지 않도록 설정
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import JsonResponse

# Create your views here.
def signup(request):
    # 회원가입 시키기
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # save의 return을 user로 받아서 로그인에 쓰겠다.
            # 가입된 유저의 Profile 레코드도 함께 생성
            Profile.objects.create(user = user)
            auth_login(request, user)
            # auth_login(request, form.get_user()) # 이렇게 써도 됨
            return redirect('posts:list')
    # 회원가입 폼 보여주기
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        # 실제 로그인(세션에 유저 정보를 넣는다.)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('posts:list')
    else:
        # 유저로부터 username과 비밀번호를 받는다.
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
    
def profile(request, username):
    # username을 가진 유저의 상세 정보를 보여주는 페이지
    # profile = User.objects.get(username=username) # 이걸 쓰지 않고
    profile = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})


def delete(request):
    # POST 계정을 삭제한다 == DB에서 user를 삭제한다
    if request.method == "POST":
        request.user.delete()
        return redirect('accounts:signup')
    
    # GET -> 진짜 삭제하시겠습니까?
    return render(request, 'accounts/delete.html')


@login_required
def follow(request, user_id):
    # User라고 쓸 수 없다.
    person = get_object_or_404(get_user_model(), pk=user_id)
    # 만약 이미 팔로우한 사람이라면
    if request.user in person.followers.all():
        # 언팔
        person.followers.remove(request.user)
    # 아니면
    else:
        # 팔로우
        person.followers.add(request.user)
    return redirect('profile', person.username)


@login_required
def vue_follow(request, user_id):
    # follow를 시키거나, unfollow 시키거나 => JSON으로 받아서 => Vue를 통해 render
    # 아래는 위 함수와 같다.
    person = get_object_or_404(get_user_model(), pk=user_id)
    # 만약 이미 팔로우한 사람이라면
    if request.user in person.followers.all():
        # 언팔
        person.followers.remove(request.user)
        followed = False
    # 아니면
    else:
        # 팔로우
        person.followers.add(request.user)
        followed = True
    return JsonResponse({'followed': followed})
    
    
@login_required
def check_follow(request, user_id):
    person = get_object_or_404(get_user_model(), pk=user_id)
    if request.user in person.followers.all():
        followed = True
    else:
        followed = False
    return JsonResponse({'followed': followed})


@login_required
def change_profile(request):
    # 프로필 정보 수정
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        return redirect('profile', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile) #OneToOne이라서 profile_set이 아니라 디폴트로 그냥 profile로 접근 가능
        return render(request, 'accounts/change_profile.html', {'profile_form': profile_form})