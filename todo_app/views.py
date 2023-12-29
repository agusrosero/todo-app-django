from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')
