from django import forms
from .models import todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'description', 'pdf_file', 'progress']



