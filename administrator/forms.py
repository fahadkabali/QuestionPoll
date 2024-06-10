from django import forms
from .models import Question, Response

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['question', 'score']
        widgets = {
            'question': forms.HiddenInput()
        }
