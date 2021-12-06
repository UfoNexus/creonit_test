from django.contrib import admin
import nested_admin

from .models import Answer, Participant, Question, Quiz


class AnswerAdmin(admin.ModelAdmin):
    """
    Вывод объектов Answer в админке.
    Также отображаются на странице вопроса и странице теста.
    """

    list_display = (
        'pk',
        'question',
        'text',
        'is_correct'
    )
    list_editable = ('is_correct',)
    search_fields = ('text', 'question')
    list_filter = ('question',)
    empty_value_display = '-пусто-'
    list_per_page = 10


class QuestionAdmin(admin.ModelAdmin):
    """
    Вывод объектов Question в админке.
    Также отображаются на странице теста.
    """

    list_display = (
        'pk',
        'quiz',
        'text',
        'order'
    )
    list_editable = ('order',)
    search_fields = ('text', 'quiz')
    list_filter = ('quiz',)
    empty_value_display = '-пусто-'
    list_per_page = 10


class AnswerInline(nested_admin.NestedTabularInline):
    """
    Добавление отображение ответов при редактировании вопроса
    """

    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedTabularInline):
    """
    Добавление отображение вопросов и ответов при редактировании теста
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
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
        'is_active'
    )
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    list_filter = ('creation_date', 'is_active',)
    empty_value_display = '-пусто-'
    list_per_page = 10


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Participant)
