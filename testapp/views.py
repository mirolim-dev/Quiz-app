from django.http import JsonResponse
from django.shortcuts import render

from .models import Question, Answer
from quizz.models import Quiz
from result.models import Result
# Create your views here.

def test_view(request, pk):
    quiz = Quiz.objects.get(id=pk)
    context = {
        'quiz': quiz
    }
    return render(request, 'test.html', context) 


def save_quiz(request, pk):
    context = {}
    if request.POST:
        questions = []
        data = request.POST
        data_ = dict(data)
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            question = Question.objects.get(id=k)
            questions.append(question)
            
            user = request.user
            quiz = Quiz.objects.get(id=pk)
            
            score = 0
            results = []
            correct_answer = None
            
            for q in questions:
                answer_selected = request.POST.get(f'{q.id}')

                if answer_selected != "":
                    answers = q.get_answers()
                    for answer in answers:
                        if answer_selected == answer.text and answer.is_correct:
                            score += 1
                            correct_answer = answer.text
                        else:
                            if answer.is_correct:
                                correct_answer = answer.text
                    results.append({q.text:{'correct_answer': correct_answer} })
                else:
                    results.append({q.text: 'Not answered'})
            
        Result.objects.create(user=user, quiz=quiz, score=score)
        
        context = {
            'score': score, 
            'results': results,
        }
    
    return JsonResponse(context)