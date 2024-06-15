from django.db import models

# Create your models here.
from django.db import models

class QuestionGroup(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Question(models.Model):
    question_group = models.ForeignKey(QuestionGroup, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    selected = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



