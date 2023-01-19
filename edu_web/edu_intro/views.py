from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import intro, Student


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


def finish(request):
    print(request)
    user = Student() #빈 객체 생성
    print("--------------------")
    print(request.POST.get('name'))
    print(request.GET.get('name'))
    print("--------------------")
    print
    user.name = request.POST.get('name')
    user.phone = request.GET.get('phone')
    user.email = request.GET.get('email')
    user.birthday = request.GET.get('birthday')
    user.school = request.GET.get('school')
    user.grade = request.GET.get('grade')
    user.way = request.GET.get('way')
    user.city = request.GET.get('city')
    user.pro_exp = request.GET.get('pro_exp')
    user.user_intro = request.GET.get('user_intro')
    user.user_motive = request.GET.get('user_motive')

    user.save()

    return render(request, 'edu_intro/register.html')
    
# def finish(request) :
#    return render(request, 'edu_intro/register.html')

