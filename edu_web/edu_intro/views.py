from django.shortcuts import render

# Create your views here.
def home_list(request) :
    return render(request, 'edu_intro/home_list.html')

def intro(request) :
    return render(request, 'edu_intro/intro.html')

def register(request) :
    return render(request, 'edu_intro/register.html')
