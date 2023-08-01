from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message, Todo

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def show_message(request):
    # DB로 부터 메세지 받아오기 (ORM 사용)
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def show_todo_title(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def show_todo_content(request, show_id):
    todo = Todo.objects.get(id = show_id)
    # print(f'클릭완료: <{todo}> {todo.id}')
    return render(request, 'todo_content.html', {'todo': todo})

def edit_todo_content(request, show_id):
    # 데이터 변경
    if request.method =='POST':
        new_content = request.POST['content']
        todo = Todo.objects.get(id = show_id)
        todo.content = new_content
        todo.save()
        # print(f'수정완료: <{todo}> {todo.id}, {todo.content}')
    return render(request, 'todo_content.html', {'todo': todo})
    # return redirect('show_todo_content')

def delete_todo(request, delete_id):
    print(f'delete_id: {delete_id}')
    todo = Todo.objects.get(id = delete_id)
    todo.delete()
    return redirect('/todos')

def add_todo(request):
    if request.method =='POST':
        new_title = request.POST['new_title']
        new_todo = Todo(title=f'{new_title}', content='')
        new_todo.save()
    return redirect('/todos')
