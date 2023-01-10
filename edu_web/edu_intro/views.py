from django.shortcuts import render
from .models import intro

# Create your views here.
def home_list(request) :
    return render(request, 'edu_intro/home_list.html')

def intro(request) :
    # intros = intro.object.all() #
    # return render(
    #     request, 'edu_intro/intro.html',
    #     {
    #         'intros' : intros,
    #     }
    #     )
    return render(request, 'edu_intro/intro.html')

def register(request) :
    return render(request, 'edu_intro/register.html')

def finish(request) :
    return render(request, 'edu_intro/finish.html')
