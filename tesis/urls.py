from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('tesis/', views.tesis,name= 'tesis'),
    path('', views.home, name='home')
]
