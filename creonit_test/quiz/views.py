from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Answer, Question, Quiz
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer


class QuizListView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
