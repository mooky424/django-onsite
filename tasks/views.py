from django.shortcuts import render, redirect
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
    form = TaskForm() 

    if request.method == "POST":
        form = TaskForm(request.POST) 
        if form.is_valid():
            task = form.save() #Model Form thingz
            return redirect('task_detail', pk=task.pk)
    
    ctx = {
        'object_list': tasks,
        "taskgroups": TaskGroup.objects.all(),
        "form" : form,
    }
    
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
        ctx['form'] = TaskForm()
        ctx['taskgroups'] = TaskGroup.objects.all()
        return ctx

    def post (self, request, *args, **kwargs):
        form = TaskForm(request.POST) 
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(**kwargs)
            ctx['form'] = form
            return self.render_to_response(ctx)
            

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_detail.html'