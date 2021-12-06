from django.contrib import admin
import nested_admin

from .models import Answer, Participant, Question, Quiz


class AnswerInline(nested_admin.NestedTabularInline):
    """
    Вывод объектов Answer в админке.
    Также отображаются на странице вопроса и странице теста.
    """

    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedTabularInline):
    """
    Вывод объектов Question в админке.
    Также отображаются на странице теста.
    """

    model = Question
    inlines = [
        AnswerInline,
    ]
    extra = 0


class QuizAdmin(nested_admin.NestedModelAdmin):
    """
    Вывод объектов Quiz в админке.
    """

    inlines = [
        QuestionInline
    ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Participant)
