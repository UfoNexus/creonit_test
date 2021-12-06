from django.urls import path
from knox import views as knox_views

from . import views

app_name = 'accounts'

urlpatterns = [
    # Страница авторизации
    path('login/', views.LoginAPI.as_view(), name='login'),

    # Выход пользователя
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),

    # Страница регистрации
    path('register/', views.RegisterAPI.as_view(), name='register'),
]
