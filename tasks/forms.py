from django import forms

from .models import Task, TaskGroup

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
