from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Answer, Question, Quiz
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer


@api_view(['GET'])
def quiz_list(request, format=None):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)
