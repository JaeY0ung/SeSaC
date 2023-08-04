from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_question_list, name='latest_question_list'),
    path('<int:question_id>/detail', views.question_detail, name='question_detail'),
    path('<int:question_id>/result', views.question_result, name='question_result'),
]