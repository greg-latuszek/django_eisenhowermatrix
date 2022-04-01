from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "important", "urgent", "completed"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "new task"}),
        }
