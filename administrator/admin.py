

from django.contrib import admin
from .models import Question, Response, Result

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'order']
    ordering = ['order']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
admin.site.register(Result)
