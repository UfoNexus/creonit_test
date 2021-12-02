from rest_framework import serializers

from .models import Answer, Question, Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        # fields = [
        #     'pk', 'title', 'slug', 'questions_count', 'description',
        #     'creation_date', 'is_active'
        # ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        # fields = [
        #     'quiz', 'text', 'order'
        # ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
