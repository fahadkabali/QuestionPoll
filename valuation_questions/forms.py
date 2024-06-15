from django import forms
from .models import Question, Choice, QuestionGroup

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date', 'text']
        widgets = {
            'question_text': forms.Select(attrs={'class': 'form-control'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'selected']
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control'}),
            'choice_text': forms.TextInput(attrs={'class': 'form-control'}),
            'selected': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class QuestionGroupForm(forms.ModelForm):
    class Meta:
        model = QuestionGroup
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
