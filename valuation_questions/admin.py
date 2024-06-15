
from django.contrib import admin
from .models import QuestionGroup, Question, Choice


admin.site.site_header = "Admin"
admin.site.site_title = "Evaluation Admin Area"
admin.site.index_title = "Welcome to the Evaluation Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

@admin.register(QuestionGroup)
class QuestionGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'question_group', 'created_at')
    list_filter = ('question_group',)
    search_fields = ('text',)

