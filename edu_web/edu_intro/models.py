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

    class Meta:
        db_table = 'intro_db'
        verbose_name = '인트로'

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
        #return f'[{self.pk}][{self.title}]' 해당 포스트의 pk 값, 해당 포스트의 title 값


class Student(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    parents = models.CharField(max_length=10, null=True)
    birthday = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sub_phone = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=200)
    school_etc = models.CharField(max_length=200 ,null=True)
    school_city = models.CharField(max_length=100)
    school_city_etc = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=50)
    way = models.CharField(max_length=200)
    way_etc = models.CharField(max_length=200,null=True)
    recommender = models.CharField(max_length=100 ,null=True)
    pro_exp = models.CharField(max_length=1, null=True)
    pro_name = models.CharField(max_length=100, null=True)
    skill = models.CharField(max_length=500, null=True)
    skiil_degree = models.CharField(max_length=50 ,null=True)
    self_intro = models.TextField()
    self_intro2 = models.TextField(null=True,)
    self_motive = models.TextField()
    self_motive2 = models.TextField(null=True,)
    nickname = models.CharField(max_length=100, null=True,)
    privacy = models.CharField(max_length=1)
    info_noshow = models.CharField(max_length=1)
    edu_ad = models.CharField(max_length=1, null=True)
    pass_or_not = models.CharField(max_length=50)
    info_check = models.CharField(max_length=1)
    memo = models.TextField(null=True,)
    photo = models.ImageField(upload_to='edu_intro/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 처음 레코드가 생성될 떄 현재 시각으로 자동 저장
    updated_at = models.DateTimeField(auto_now=True) # 다시 저장할 떄마다 그 시각 저장
    video = EmbedVideoField()

    class Meta:
        db_table = 'student_db'
        verbose_name = '신청자'

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
        #return f'[{self.pk}][{self.title}]' 해당 포스트의 pk 값, 해당 포스트의 title 값
        user

