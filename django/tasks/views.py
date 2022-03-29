from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task
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
class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(author=self.request.user)
