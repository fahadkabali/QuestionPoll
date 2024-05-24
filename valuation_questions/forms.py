from django import forms
from .models import Response, Option

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['selected_option']

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['selected_option'].queryset = Option.objects.filter(question=question)
