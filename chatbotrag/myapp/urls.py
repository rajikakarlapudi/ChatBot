from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('success/', views.success, name='success'),
    path('list_files/', views.list_files, name='list_files'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
