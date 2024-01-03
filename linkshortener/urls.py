from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener.urls')),  # Certifique-se de que a importação esteja correta
]
