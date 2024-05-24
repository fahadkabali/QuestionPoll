from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Question, Option, Response, Feedback

# Customize User Admin (optional)
admin.site.site_header = "Evaluation Admin"
admin.site.site_title = "Administrator Area"
admin.site.index_title = "Welcome to the MIlima Admin Area"

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.unregister(settings.AUTH_USER_MODEL)  # Unregister default UserAdmin
admin.site.register(settings.AUTH_USER_MODEL, UserAdmin)  # Register custom UserAdmin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    search_fields = ('text',)
    ordering = ('-created_at',)  # Order by newest questions first

class OptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'Option_list')  # Consider renaming Option_list to a more descriptive field name
    search_fields = ('text',)
    list_filter = ('question',)
    autocomplete_fields = ('question',)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'get_selected_option', 'created_at')
    search_fields = ('user__username', 'question__text')
    list_filter = ('user', 'question')
    readonly_fields = ('user', 'question', 'get_selected_option')

    def get_selected_option(self, obj):
        return obj.selected_option.text
    get_selected_option.short_description = 'Selected Option'

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('response', 'feedback_text', 'satisfaction_score', 'created_at')
    search_fields = ('response__user__username', 'response__question__text', 'feedback_text')
    list_filter = ('response__question', 'satisfaction_score')
    readonly_fields = ('response', 'created_at')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Feedback, FeedbackAdmin)
