from django.contrib import admin
from .models import Posting, Comment


# Register your models here.
# created at, updated at을 보여주는 기능
class PostingModelAdmin(admin.ModelAdmin): # 이름은 이렇게 짓는 게 컨벤션
    readonly_fields = ('created_at', 'updated_at')  # 레코드 개별화면 확인
    list_display = ('id', 'content', 'created_at', 'updated_at')  # 리스트에서 표시할 컬럼
    list_display_links = ('id', 'content')  # 리스트에서 clickable 할 속성


admin.site.register(Posting, PostingModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')  # 레코드 개별화면 확인
    list_display = ('id', 'posting', 'content', 'created_at', 'updated_at')  # 리스트에서 표시할 컬럼
    list_display_links = ('id', 'content')  # 리스트에서 clickable 할 속성


admin.site.register(Comment, CommentModelAdmin)
