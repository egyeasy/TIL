from django.shortcuts import render, get_object_or_404, redirect
from .models import Posting, Comment


# Create your views here.
def posting_list(request):
    postings = Posting.objects.all().order_by('-updated_at')  # 마지막으로 수정한 것이 맨 위에 옴
    return render(request, 'sns/list.html', {
        'postings': postings,
    })


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all().order_by('-created_at')

    return render(request, 'sns/detail.html', {
        'posting': posting,
        'comments': comments,
    })


def create_posting(request):
    if request.method == 'POST':
        # create 메서드도 내장적으로 save()를 쓴다. 그래서 오버라이드 한 save가 적용돼서 print 된다.
        posting = Posting.objects.create(  # 객체를 받아서 해당 id로 redirect 하는 데 쓴다
            content=request.POST.get('content'),
            icon=request.POST.get('icon'),
            image=request.FILES.get('image'),  # POST가 아니라 FILES에서 가져온다
        )
        return redirect('sns:posting_detail', posting.id)
    else:
        return redirect('sns:posting_list')


def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('comment')
        comment.posting = posting
        comment.save()
    return redirect('sns:posting_detail', posting.id)

