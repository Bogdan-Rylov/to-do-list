from django import forms

from to_do.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "date_deadline", "is_done", "tags",)
        widgets = {
            "date_deadline": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
        }
