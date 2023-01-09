from django.shortcuts import render
from .models import intro

# Create your views here.
def home_list(request) :
    return render(request, 'edu_intro/home_list.html')

def intro(request) :
    intros = intro.object.all() # intro에 모든 레코드를 가져와 intros에 저장 render() 함수 안에 posts를 딕셔너리 형태로 추가
    return render(
        request, 'edu_intro/intro.html',
        {
            'intros' : intros,
        }
        )

def register(request) :
    return render(request, 'edu_intro/register.html')

def finish(request) :
    return render(request, 'edu_intro/finish.html')
