from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encurtar/', views.encurtar, name='encurtar'),
    path('<str:codigo_hash>/', views.redirecionar, name='redirecionar'),
]
