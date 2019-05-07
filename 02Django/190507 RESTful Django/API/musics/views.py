from django.shortcuts import render, get_object_or_404
from .serializer import MusicSerializer
from rest_framework.response import Response
from .models import Music
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def music_list(request):
    # 여기서 쓰는 ORM 작업 정의 : 모든 음악들을 가져온다.
    musics = Music.objects.all()
    
    # 예전의 html 버전 같았으면
        # return render(request, 'list.html', {'musics': musics})
    # 여기서는 json을 만들어서 던져줄 것
    serializer = MusicSerializer(musics, many=True)  # 인자(무엇을시리얼라이즈할지, 여러개인지한개인지)
    return Response(data=serializer.data)  # 시리얼라이저 안의 데이터를 인자로 넣어준다.
    

@api_view(['GET'])
def music_detail(request, music_id):
    # music_id에 있는 값으로 music을 찾아 가져온다.
    music = get_object_or_404(Music, pk=music_id)
    serializer = MusicSerializer(music)  # many=False가 default
    return Response(data=serializer.data)
    