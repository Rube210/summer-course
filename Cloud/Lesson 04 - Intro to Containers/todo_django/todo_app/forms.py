from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "dueDate"]
        widgets = {
            "dueDate": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
