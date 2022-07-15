from tabnanny import verbose
from django.db import models
from quizz.models import Quiz
# Create your models here.

class Question(models.Model):
    class Meta:
        verbose_name_plural = 'Questions'
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.text}"
    
    def get_answers(self):
        return self.answer_set.all().order_by('?')
    


class Answer(models.Model):
    class Meta:
        verbose_name_plural = 'answers'
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    is_correct = models.BooleanField()
    
    def __str__(self):
        return self.text
    
    
    