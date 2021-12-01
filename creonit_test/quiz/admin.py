from django.contrib import admin
import nested_admin

from .models import Answer, Participant, Question, Quiz


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [
        AnswerInline,
    ]
    extra = 0


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        QuestionInline
    ]


admin.site.register(Quiz, QuizAdmin)
