from django.db import models
from django.contrib.auth.models import User
from quizz.models import Quiz
# Create your models here.

class Result(models.Model):
    class Meta:
        verbose_name_plural = 'Results'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.quiz}'