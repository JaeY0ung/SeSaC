#? 내기 만드는 폴더
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name = 'hello_world'),
    path('messages/', views.show_message, name = 'show_message'),

    path('todos/',                       views.show_todo_title,   name = 'show_todo_title'),
    path('todos/<show_id>/content',      views.show_todo_content, name = 'show_todo_content'),
    path('todos/<show_id>/content/edit', views.edit_todo_content, name = 'edit_todo_content'),
    path('todos/<delete_id>/delete/',    views.delete_todo,       name = 'delte_todo'),
    path('todos/add_todo',               views.add_todo,          name = 'add_todo'),
]