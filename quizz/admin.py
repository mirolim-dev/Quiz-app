from django.contrib import admin
from .models import Quiz
# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'topic', 'time', 'max_score', 'type', 'created_at']
    
admin.site.register(Quiz, QuizAdmin)