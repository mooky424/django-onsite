from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskForm

from .models import Task, TaskGroup

def index(request):
    return HttpResponse('Hello World')

def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        'object_list': tasks,
        "taskgroups": TaskGroup.objects.all(),
        "form" : form,
    }
    if request.method == "POST":
        form = TaskForm(request.POST) 
        if form.is_valid():
            form.save() #Model Form thingz
    
    return render(request, 'task_list.html', ctx)

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    ctx = {
        'task' : task
    }

    return render(request, 'task_detail.html', ctx)

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['taskgroups'] = TaskGroup.objects.all()
        ctx['form'] = TaskForm()
        return ctx

    def post (self, request, *args, **kwargs):
        form = TaskForm(request.POST) 
        if form.is_valid():
            task = Task()
            task.name = form.cleaned_data["name"]
            task.due_date = form.cleaned_data["due_date"]
            task.taskgroup = form.cleaned_data["taskgroup"]
            task.save()

        return self.get(request, *args, **kwargs)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create.html'


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_detail.html'