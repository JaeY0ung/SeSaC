from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def todo_detail(request, pk):
    task = get_object_or_404(Task, pk=pk) #? task = Task.objects.all(id = pk)와 같음
    return render(request, 'todo/todo_detail.html', {'task': task})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']  #? POST는 무조건 대문자로 써야 한다.
        description = request.POST['description']
        task = Task.objects.create(title = title, description = description)
        #? task.save() : 수정될 때만 사용 (만들어질 때는 사용 X)
        return redirect('todo_detail', pk=task.pk)
    return render(request, 'todo/todo_create.html')


def todo_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/todo_update', {'task': task})

def todo_delete(request, pk):
    return render(request,)