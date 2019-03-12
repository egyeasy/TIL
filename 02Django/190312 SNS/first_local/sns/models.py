from django.db import models

# ImageKit - resize image
from imagekit.models import ImageSpecField, ProcessedImageField  # 두 가지 클래스 import
from imagekit.processors import ResizeToFit


# Create your models here.
class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=20, default='fas fa-question') # fontawesome 이모티콘 지정해주고 default 값 설정
    # upload url => /media/posting/origin/yyyymmdd/
    # image = models.ImageField(blank=True, upload_to='posting/origin/%Y%m%d') # 원본을 저장하는 코드

    # resize image - 원본 대신
    image = ProcessedImageField(
        upload_to='posting/resize/%Y%m%d',
        processors=[ResizeToFit(width=960, upscale=False)],
        format='JPEG'
    )

    # thumbnail
    image_thumbnail = ImageSpecField(  # 기존에 있던 이미지(하나의 origin)를 가지고 작업하는 것
        source='image',  # 이미지를 가져올 컬럼 명을 써줄 것
        processors=[ResizeToFit(width=320, upscale=False)],
        format='JPEG',
        options={'quality': 60}  # 화질 등 60퍼센트로 축소
    )


    # 자동으로 시간 잡아줌
    created_at = models.DateTimeField(auto_now_add=True) # 저장되는 시점을 넣어줌
    updated_at = models.DateTimeField(auto_now=True) # 저장 or 수정된 시점을 넣어줌

    def __str__(self):
        return f'{self.id}: {self.content[:20]}'

    def save(self, *args, **kwargs):
        # 여기에 욕설이 들어왔을 때 저장하기 전에 처리하는 등의 작업을 할 수 있다.
        super().save(*args, **kwargs)  # 기존의 저장 기능
        print()
        print(f'=== Saved Posting with id: {self.id}')
        print(f'    content: {self.content}')
        if self.image:
            # 1024로 나누면 KB가 됨
            print(f'    image_size: {self.image.width}px * {self.image.height}px: {round(self.image.size / 1024)}kb')
        print('===============================')
        print()


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.posting.content[:10]}: {self.content[:20]}'

