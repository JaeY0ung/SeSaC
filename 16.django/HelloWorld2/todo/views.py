from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    # task = Task.objects.all(id = pk)
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']  #? POST는 무조건 대문자로 써야 한다.
        description = request.POST['description']
        task = Task.objects.create(title = title, description = description)
        #? task.save() : 수정될 때만 사용 (만들어질 때는 사용 X)
        return redirect('task_detail', pk=task.pk)
    return render(request, 'todo/task_create.html')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_update', {'task': task})

def task_delete(request, pk):
    return render(request,)