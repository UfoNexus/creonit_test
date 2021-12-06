from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('quiz.urls',
                     namespace='quiz')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('account/', include('accounts.urls',
                             namespace='accounts'))
]
