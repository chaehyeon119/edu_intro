from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('intro', views.intro, name='intro.html'),
    path('register', views.register, name='register.html'),

]