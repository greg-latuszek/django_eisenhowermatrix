from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'  # placeholder="new task"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'new task'}),
        }
