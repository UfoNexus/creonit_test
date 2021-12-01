from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    questions_count = models.IntegerField(default=0)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:100]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:100]


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    if_completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
