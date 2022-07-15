from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'quizes'
    name = models.CharField(max_length=80, null=True)
    image = models.ImageField(upload_to='images/quizz', null=True, blank=True)
    topic = models.CharField(max_length=120, null=True)
    time = models.PositiveBigIntegerField(help_text='duration time by minutes', null=True)
    max_score = models.PositiveBigIntegerField()
    
    DIF_CHOISES = (
        ('easy', 'easy'),
        ('normal', 'normal'),
        ('expert', 'expert'),
    )
    type = models.CharField(max_length=7, choices=DIF_CHOISES, default='easy')
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name
    
    def get_questions(self):
        return self.question_set.all().order_by('?')
    
    