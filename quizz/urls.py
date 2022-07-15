from urllib.parse import urlparse
from django.urls import path
from .views import home, QuizListView
urlpatterns = [
    # path('', home, name='home'),
    path('', QuizListView.as_view(), name='home')
]
