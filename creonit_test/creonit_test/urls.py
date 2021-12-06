from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Включение путей приложения quiz
    path('', include('quiz.urls',
                     namespace='quiz')),

    # Панель администратора
    path('admin/', admin.site.urls),

    # Штатная авторизация DRF. Не отключаю, так как сессия пользователя,
    # которой управляет приложения accounts слетает после обновления страницы
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

    # Включение путей приложения accounts (управление пользователями)
    path('account/', include('accounts.urls',
                             namespace='accounts'))
]
