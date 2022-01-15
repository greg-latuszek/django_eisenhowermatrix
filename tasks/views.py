from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView

from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # will write to DB
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)
