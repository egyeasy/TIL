from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutForm, ShoutModelForm

# Create your views here.
def home(request):
    # form 보여주기 & 문의사항 전부 보여주기
    # form = ShoutForm()  # initialize
    shouts = Shout.objects.all()
    form = ShoutModelForm()
    context = {
        'shouts': shouts,
        # 'form': form,  # form을 html에서 쓰겠다
    }
    return render(request, 'shouts/home.html', context)


def create(request):
    # POST : 글을 DB에 저장
    if request.method == "POST":
        # home의 로직을 그대로 가져오면 됨
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')

    # GET : 글 작성할 수 있는 form
    else:
        form = ShoutModelForm()
        context = {
            'form': form
        }
        return render(request, 'shouts/form.html', context)




def update(request, id):
    shout = Shout.objects.get(pk=id) # 양쪽 공통이므로 맨 위에 써준다
    # 수정 반영하기(update)
    if request.method == "POST":
        # 인자 - 날아온 데이터, 수정할 인스턴스(생성에 비해 인자가 하나 더 필요) -> 알아서 update로 처리
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
        return redirect('shouts:home')

    # 편집하기(edit)
    else:
        form = ShoutModelForm(instance=shout)  # instance shout 지정해주면 form 안에 이 shout를 넣어서 html에 넣어줌
        # default 값을 여기서 넣어서 전달 가능하다.
        context = {
            # 'shout': shout,
            'form': form,
        }
        return render(request, 'shouts/form.html', context)