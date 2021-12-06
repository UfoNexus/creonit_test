from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Quiz
from .permissions import IsAdminOrReadOnly
from .serializers import ParticipantSerializer, QuizSerializer


class QuizListView(generics.ListCreateAPIView):
    """
    Вывод страницы списка тестов
    """

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminOrReadOnly]


class QuizView(generics.GenericAPIView):
    """
    Обработка детальной страницы теста
    """

    lookup_field = 'slug'
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, slug):
        """
        Поиск необходимого теста по slug
        :param slug: ссылка на тест
        :return: объект модели Quiz
        """

        try:
            return Quiz.objects.get(slug=slug)
        except Quiz.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        """
        Вывод детальной страницы теста
        :param request: требуемый аргумент, содержащий запрос
        :param slug: ссылка на тест
        :return: словарь с данными выбранного теста
        """

        quiz = self.get_object(slug)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    def put(self, request, slug):
        """
        Редактирование теста с открытой страницы
        :param request: требуемый аргумент, содержащий запрос
        :param slug: ссылка на тест
        :return: словарь с новыми данными выбранного теста
        """

        quiz = self.get_object(slug)
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, slug):
        """
        Попытка реализовать прохождение теста пользователем
        """

        pass
        # participant = get_object_or_404(User, username='admin')
        # serializer = ParticipantSerializer(participant, data=request.data)
        #
        # return Response(serializer.initial_data)
