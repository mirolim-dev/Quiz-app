from django.urls import path
from .views import test_view, save_quiz
urlpatterns = [
    path('<pk>/', test_view, name='test_view'),
    path('<pk>/save', save_quiz, name='save-quiz'),
]
# test
