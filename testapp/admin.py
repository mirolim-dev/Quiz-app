from django.contrib import admin
from .models import Question, Answer
# Register your models here.
class AnswerAdmin(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    list_display = ['id', 'quiz', 'text']

admin.site.register(Question, QuestionAdmin)