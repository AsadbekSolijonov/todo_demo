from task.models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done', 'is_delete']
        # formaga css qo'shish
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavha...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'placeholder': 'Tavsif...'}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_delete': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

