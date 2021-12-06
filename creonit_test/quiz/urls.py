from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'quiz'

urlpatterns = [
    # Страница списка тестов
    path('quiz_list/', views.QuizListView.as_view(), name='quiz_list'),

    # Детальная страница выбранного теста
    path('quiz/<slug:slug>', views.QuizView.as_view(), name='quiz'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
