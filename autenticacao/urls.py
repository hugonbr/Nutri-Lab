from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
]