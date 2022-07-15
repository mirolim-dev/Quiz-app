from django.contrib import admin
from .models import Result
# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz', 'score', 'created_at']
    
admin.site.register(Result, ResultAdmin)