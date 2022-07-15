from django.shortcuts import render
from django.views.generic import ListView
from .models import Quiz

# Create your views here.
def home(request):
    quizes = Quiz.objects.all()
    
    context = {
        'quizes': quizes,
    }
    return render(request, 'home.html', context)

class QuizListView(ListView):
    model = Quiz
    template_name = 'home.html'