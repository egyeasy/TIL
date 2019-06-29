from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # 여기 User와는 다른 User여야 한다. 
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")


class Profile(models.Model):
    description = models.TextField(blank=True) # 안 써도 됨
    nickname = models.CharField(max_length=40, blank=True) # 안 써도 됨
    # User와의 관계 설정 - reference 대상(User in models.py), cacade
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 프로필 이미지
    image = models.ImageField(upload_to='profile/')
    
    def __str__(self):
        return f"<{self.user.username}>, nickname: {self.nickname}, description: {self.description}"