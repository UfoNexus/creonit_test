from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    """
    Модель теста
    """

    title = models.CharField(max_length=150)
    slug = models.SlugField()
    questions_count = models.IntegerField(default=0)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-creation_date']
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Модель вопроса для объекта модели Quiz
    """

    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE,
                             related_name='questions')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:100]


class Answer(models.Model):
    """
    Модель ответа для объекта модели Question
    """

    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:100]


class Participant(models.Model):
    """
    Модель пользователя, который прошел тест.
    (!!!) На данный момент не используется, так как не реализована
    механика прохождения теста пользователем.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    picked_answers = models.ManyToManyField(Answer,
                                            symmetrical=False)
    if_completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
