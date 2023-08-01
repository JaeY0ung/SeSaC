#? 내기 만드는 폴더
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('messages/', views.show_message, name='show_message'),
]