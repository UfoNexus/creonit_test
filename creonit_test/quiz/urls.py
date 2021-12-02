from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'quiz'

urlpatterns = [
    path('quiz_list/', views.quiz_list, name='quiz_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
