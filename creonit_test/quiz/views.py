from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .models import Answer, Question, Quiz
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer

def quiz_list(request):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return JsonResponse(serializer.data, safe=False)
