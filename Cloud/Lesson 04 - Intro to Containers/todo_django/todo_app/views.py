from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Task
from django.template import loader
from .forms import TaskForm


def index(request):
    return render(request, "todo_app/main.html")


def all_tasks(request):
    all_tasks = Task.objects.order_by("dueDate")
    context = {"all_tasks": all_tasks}
    return render(request, "todo_app/task_list.html", context)


def task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        context = {"task": task}
    except Task.DoesNotExist:
        raise Http404("Task does not exist or is not authorized.")
    return render(request, "todo_app/task.html", context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # Save the new task and redirect to the task list
            form.save()
            return redirect("all_tasks")
    else:
        form = TaskForm()
    return render(request, "todo_app/task_create.html", {"form": form})