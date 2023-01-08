from django.db import models
from django.conf import settings

# Create your models here.
#글을 만들건데 어떤 형태가 있는지 틀을 잡아주는 과정
class myText(models.Model) :

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    head_image = models.ImageField(upload_to='edu_intro/images/%Y/%m/%d/', blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title