from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # print(dir(form))
            eisenh_task = form.save(commit=False)  # will not write to DB
            eisenh_task.author = request.user
            eisenh_task.save()  # will write to DB
        else:
            print(form.errors)
        view_variant = request.POST["view_variant"]  # preserve presentation layout
        return redirect(f'/?view={view_variant}')

    view_variant = request.GET.get('view', 'table')
    context = {'tasks': tasks, 'form': form, 'view': view_variant}
    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)


# Celery
def show_primes(request, x):
    from .tasks import print_primes

    print_primes.delay(x)
    return redirect('/')


# DRF
@api_view(["GET"])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    content = {
        "tasks": serializer.data,
    }
    return Response(content)
