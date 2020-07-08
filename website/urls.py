from django.urls import path

app_name = 'website'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maratona/', views.listclass, name='listclass'),
]