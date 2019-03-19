from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    # todos에 있는 내용을 다 가져와 보여주기(id 기준 내림차순 정렬)
    # todos = Todo.objects.all().order_by('-id')
    # todos = Todo.objects.filter(user_id=request.user.id).all()
    todos = request.user.todo_set.all() # anonymous의 경우 todo_set이 없음 - 처리해줄 것
    context = {
        'todos': todos
    }
    return render(request, 'todos/home.html', context)


def create(request):
    # todos 작성하기
    content = request.POST.get('content')
    # completed = request.POST.get('completed')
    # 현재 접속해있는 유저의 아이디
    user_id = User.objects.first().id # 이건 첫번째 유저만 가져온다!
    current_user_id = request.user.id
    Todo.objects.create(content=content, user_id=current_user_id)

    return redirect('todos:home')


def check(request, id):
    # 특정 id를 가진 todo를 뽑아 completed = True 로 만들어주기
    todo = Todo.objects.get(pk=id)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:home')


def delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('todos:home')