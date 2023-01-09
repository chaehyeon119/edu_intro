from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField

# Create your models here.
#글을 만들건데 어떤 형태가 있는지 틀을 잡아주는 과정
class intro(models.Model) :

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    img_url = models.CharField(max_length=200)
    head_image = models.ImageField(upload_to='edu_intro/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 처음 레코드가 생성될 떄 현재 시각으로 자동 저장
    updated_at = models.DateTimeField(auto_now=True) # 다시 저장할 떄마다 그 시각 저장
    video = EmbedVideoField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
        #return f'[{self.pk}][{self.title}]' 해당 포스트의 pk 값, 해당 포스트의 title 값